---
layout: post
title:  "PRACE Summer School of HPC Blog #2"
summary: "First week of studying"
author: ledmington
date: '2022-07-16 10:50:00 +0000'
category:
 - blog
 - prace
 - hpc
 - matrix
 - rsb
thumbnail: /assets/img/sohpc-logo.png
keywords: blog, prace, hpc
permalink: /blog/summer-school-week-2/
usemathjax: true
---

I spent most of the time this week studying the theory behind the `librsb` library and finding the right place where to start my job.

## What is a sparse matrix?
A matrix is said to be sparse when *most of its elements* are zero. "Most of its elements" is not an objective or numerical way to define it so, by convention, the number of non-zero elements of a sparse matrix must be comparable to the number of rows and/or columns of matrix itself. If the matrix doesn't have this property, it is called *dense*. I understand that this doesn't make the definition objective, too, but the *sparsity* of a matrix is not a *strong mathematical property* like "you can't multiply a sparse matrix and a dense one".

## Why should we treat these matrices differently?
For the same reason we compress images or videos. And also for optimizing the cache hit ratio, actually.

In each school where linear algebra is taught, they obviously teach matrix multiplication. If you've ever done a matrix multiplication by hand, you probably have noticed how fast it becomes when the matrices have a lot of zero elements inside. For each zero element, you can skip its multiplication with the corresponding element in the other matrix. And, if you have an entire row or column filled with zeroes, you can skip that part entirely and place a zero in the resulting matrix.

When you have so many zero elements, you may want to exploit them by skipping many useless iteration of the algorithm. The naive algorithm for matrix multiplication (which looks like the one below) doesn't have any `if`s inside, so multiplying two zero-matrices or two *normal* ones will take the same time.
```c
for (int i=0; i < rows; i++) {
    for (int j=0; j < columns; j++) {
        result[i][j] = 0;
        for (int k=0; k < N; k++) {
            result[i][j] += X[i][k] * Y[k][j];
        }
    }
}
```

Even if we wanted to implement a *row skip* when there are only zeroes, we should look into all the elements before multiplying them. It's a $$O(n)$$ best-case optimization for $$O(n)$$ operation, so obviously it doesn't work. We need something like an $$O(1)$$ optimization in order to go faster.

Introducing the COO format. COO is a bad acronym for "coordinate list". The description of this matrix storing format is literally "you memorize only the non-zero elements of the matrix, each one with its row index and column index, sorted by row index first and then by column index". From the explanation you may think of it like a literal list, an Array-of-Structures composed of triples like $$(r, c, value)$$ but it's often implemented in a Structure-of-Arrays fashion to optimize parallel accesses. Below there's a simple example of the conversion of a matrix from *normal* to COO format (with zero-based indices).
```
Original matrix
0 0 3 7 0
2 0 0 0 0
0 5 0 0 0
0 0 6 0 0
0 8 0 0 0

COO format
row_index:    0 0 1 2 3 4
column_index: 2 3 0 1 2 1
value:        3 7 2 5 6 8
```

Now let's do some calculations. To compute how many bytes we saved by using the COO format. Let's define:
 - $$R$$ as the number of rows of the original matrix
 - $$C$$ as the number of columns of the original matrix
 - $$N$$ as the number of non-zero elements inside the matrix
 - $$I$$ as the number of bytes required to store an index (for rows and columns)
 - $$K$$ as the number of bytes required to store an element of the matrix

To store the original matrix we need $$O(K\cdot R\cdot C)$$ bytes while to store the matrix in COO format we need $$O((2I+K)\cdot N)$$ bytes. In order to actually save some space by using this format, the following relation must be true $$N < \frac{KRC}{2I+K}$$
I understand that it's difficult to imagine with all these variables, so let's add some numbers. Usually, the index of something is stored as an `int` or `unsigned int`: in either case, they need 4 bytes so we substitute $I$ with 4.
If we stored the values as `float`s, they would require 4 bytes each, so the relation becomes $$N < \frac{RC}{3}$$ while, if we needed more precision and stored the values as `double`s, they would require 8 bytes each, so the relation would become $$N < \frac{RC}{2}$$

All of this means that, in order to save space on the computer, the number of non-zero elements must not exceed 33% of all elements (in case of `float`s) and 50% of all elements (in case of `double`s). That's a pretty wide range considering that we're using sparse matrices which have enough non-zero elements to fill 2 or 3 rows/columns at most.

Why is this better for the time complexity?

In case you needed further memory optimization, somebody invented the CSR and CSC formats: Compressed Sparse Rows and Compressed Sparse Columns, respectively. These two optimize the memory required in case of a sparse matrix with more dense rows/columns than sparse ones, but I'm not going to explain them.

That's it for this week, stay tuned and don't miss the next post!