---
layout: post
title:  "How to read a file in parallel"
summary: "Is it possible?"
author: ledmington
date: '2022-04-13 09:13:00 +0000'
category:
 - parallel
 - file
thumbnail: /assets/img/file-parallel.png
keywords: parallel, file
permalink: /blog/parallel-read-a-file/
usemathjax: true
---

# The problem
The problem is as simple as this question:
> **Is it possible to read a file in parallel?**

While it may seem really trivial, once you start thinking about the way a hard drive (or an SSD) works a lot of doubts start to rise.

In order to compare execution times we need a fake task to perform with some fake data. For simplicity, we generate a file with random unsigned integers and we want to find the minimum of them.

# The proposed solutions
## Reading serially
The most simple way to process a file.
1. Read one line
2. Perform the computation
3. If you're not at the end of the file, go to step 1

```c
unsigned int read_serially(const char *filename) {
    unsigned int best = UINT_MAX;
    FILE *f = fopen(filename, "r");
    unsigned int n;
    while(1 == fscanf(f, "%u\n", &n)) {
        best = min(best, n);
    }
    fclose(f);
    return best;
}
```

## Partition (logically) the file with pointers
We start with a classic parallel pattern: **partition**.

The file is partitioned like an array in the RAM. Each one of the N threads reads $$1/N$$ of the file's content. At the end, a min-reduction is performed to gather the local results.

```c
unsigned int partition_logically(const char *filename) {
    unsigned int best = UINT_MAX;
    const long unsigned int length = get_file_size(filename);
    #pragma omp parallel default(none) \
    shared(filename, length) \
    reduction(min:best)
    {
        FILE *f = fopen(filename, "r");
        const unsigned int idx = omp_get_thread_num();
        const long unsigned int portion = length / omp_get_num_threads();
        const long unsigned int start = portion * idx;
        fseek(f, start, SEEK_SET);
        unsigned int n;
        for(long unsigned int i=start; i<start+portion; i++) {
            fscanf(f, "%u\n", &n);
            best = min(best, n);
        }
        fclose(f);
    }
    return best;
}
```

## Read different copies at different locations
Create an exact copy of the entire file for each thread and then make that thread read only a portion of it, like if it was partitioned. At the end, a min-reduction is performed to gather the local results.

```c
unsigned int copy_and_partition(const char *filename) {
    unsigned int best = UINT_MAX;
    const unsigned int nth = omp_get_max_threads();
    const long unsigned int length = get_file_size(filename);
    char copies_names[nth][11];
    FILE *copies[nth];
    FILE *main = fopen(filename, "r");

    // Creating copies
    for(unsigned int i=0; i<nth; i++) {
        sprintf(copies_names[i], "tmp%02u.txt", i);
        copies[i] = fopen(copies_names[i], "w");
    }

    // Copying content
    while(!feof(main)) {
        char ch = fgetc(main);
        for(unsigned int i=0; i<nth; i++) {
            fputc(ch, copies[i]);
        }
    }

    // Closing files
    for(unsigned int i=0; i<nth; i++) {
        fclose(copies[i]);
    }
    fclose(main);

    #pragma omp parallel default(none) \
    shared(length, copies, copies_names) \
    reduction(min:best)
    {
        const unsigned int idx = omp_get_thread_num();
        copies[idx] = fopen(copies_names[idx], "r");
        const long unsigned int portion = length / omp_get_num_threads();
        const long unsigned int start = portion * idx;
        fseek(copies[idx], start, SEEK_SET);
        unsigned int n;
        for(long unsigned int i=start; i<start+portion; i++) {
            fscanf(copies[idx], "%u\n", &n);
            best = min(best, n);
        }
        fclose(copies[idx]);
    }
    return best;
}
```

## Physical partitions
Partition the files into physical smaller files (one for each thread) and then let each thread process the entire small file serially. This one is exactly like the "Logic Partitions" but each one is firstly dumped into a separate file. This should highlight any software-level or OS-level mutex-like behavior related to single files.

At the end, a min-reduction is performed to gather the local results.

```c
unsigned int split_and_read(const char *filename) {
    unsigned int best = UINT_MAX;
    const unsigned int nth = omp_get_max_threads();
    char copies_names[nth][11];
    FILE *copies[nth];
    FILE *main = fopen(filename, "r");

    // Creating copies
    for(unsigned int i=0; i<nth; i++) {
        sprintf(copies_names[i], "tmp%02u.txt", i);
        copies[i] = fopen(copies_names[i], "w");
    }

    // Copying content
    long unsigned int line = 0;
    unsigned int n;
    while(1 == fscanf(main, "%u\n", &n)) {
        fprintf(copies[line%nth], "%010u\n", n);
        line++;
    }

    // Closing files
    for(unsigned int i=0; i<nth; i++) {
        fclose(copies[i]);
    }
    fclose(main);

    #pragma omp parallel default(none) \
    shared(copies, copies_names) \
    reduction(min:best)
    {
        const unsigned int idx = omp_get_thread_num();
        copies[idx] = fopen(copies_names[idx], "r");
        unsigned int n;
        while(1 == fscanf(copies[idx], "%u\n", &n)) {
            best = min(best, n);
        }
        fclose(copies[idx]);
    }
    return best;
}
```

# Time comparison
The file generated to take these times contained $$10^8$$ numbers.

## On SSD
These results come from my PC with 8-core CPU and an SSD.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-7btt">Name</th>
    <th class="tg-7btt">Time</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">Serial</td>
    <td class="tg-7btt">8.768 s</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Logical<br>partitions</td>
    <td class="tg-7btt">17.732 s</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Partition<br>copies</td>
    <td class="tg-7btt">177.84 s</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Split and read</td>
    <td class="tg-7btt">23.872 s</td>
  </tr>
</tbody>
</table>

## On HDD
These results come from my PC with 4-core CPU and an HDD.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-7btt">Name</th>
    <th class="tg-7btt">Time</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow">Serial</td>
    <td class="tg-7btt">14.347 s</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Logical<br>partitions</td>
    <td class="tg-7btt">42.773 s</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Partition<br>copies</td>
    <td class="tg-7btt">256.308 s</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Split and read</td>
    <td class="tg-7btt">55.722 s</td>
  </tr>
</tbody>
</table>

# The final answer
It appears from the results that the serial read is the fastest way to read a file. The logical partitions would have had better results if we didn't count the time to create N file pointers and to move them.

The (relatively) slight time difference between "Logical partitions" and "Split and read" makes me think that, even with separate files that could be cached in memory separately, the threads still concur on some resource when reading their own file copy. I think that this *shared resource* might be the hard drive itself, or its controller's software, which serves reads and writes serially with a FIFO queue. In order to confirm this assumption, I would need to test this code with different file copies placed **on entirely different hard drives** but, unfortunately, I only have one-drive PCs.

Lastly, we can safely say that the huge time difference between "Partition copies" and all the others is due to the process of creating N full copies of the input file.

**NOTE**: the source code for this experiment is available [here](https://github.com/Ledmington/personal/blob/main/parallel_file/parallel_file.c).