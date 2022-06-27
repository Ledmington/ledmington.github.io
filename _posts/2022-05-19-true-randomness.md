---
layout: post
title:  "How to get a \"true\" random number generator"
summary: "No libraries required."
author: ledmington
date: '2022-04-13 13:40:00 +0000'
category:
 - randomness
thumbnail: /assets/img/file-parallel.png
keywords: randomness, generator
permalink: /blog/true-randomness/
usemathjax: true
published: false
---

# The idea
Every programmer, at least once, encounters the problem with randomness in computers. The random number generators (RNG) available in computers are not really random. That's why they are called pseudo-random number generators (PRNG). This means that they use a deterministic algorithm to generate numbers and the whole randomness is "guaranteed" as long as the seed is "random enough". Since the algorithm is deterministic, a certain seed will always generate the same sequence of numbers: this feature is really useful for testing the behavior of programs in a predictable way but using the same the same seed is not a good idea to have good randomness. Usually, in order to have a "fairly good" randomness, the current timestamp is used as the seed.

The PRNG implemented in the C standard library generates a fairly good uniform distribution as you can see by compiling and running this simple program.
```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>
#include <string.h>

int main(void) {
    srand(time(NULL));

    const unsigned int size = 1 << 20;

    unsigned int v[size];
    memset(v, 0, size * sizeof(unsigned int));

    const unsigned long long int n = 1234567890;

    for (unsigned int k=0; k<100; k++) {
        for (unsigned long long int i=0; i<n/100; i++) {
            v[rand() & (size-1)]++;
        }
        printf("%u%% done\n", k+1);
    }

    unsigned int min = UINT_MAX;
    unsigned int max = 0;
    for (unsigned int i=0; i<size; i++) {
        if(v[i] > max) max = v[i];
        else if(v[i] < min) min = v[i];
    }
    const unsigned int diff = max - min;

    printf("Max value: %u\n", max);
    printf("Min value: %u\n", min);
    printf("Max difference: %u (%.10f%%)\n", diff, (double)diff / (double)n);

    return EXIT_SUCCESS;
}
```

I'm not saying that I can do better, but my idea is about a real RNG and how to obtain it with a common computer. With a bit of research I found out how professionals (usually companies that offer cryptography services) generate real random numbers. The trick is only about what source of randomness to use because, if have one, you can fiddle with bits as many times as you want to improve it.

We start with [random.org](https://www.random.org/) which is a famous website that generates random numbers of various types. As they explain in the first few lines of the home page, the randomness is taken from atmospheric noise. This means, as far as I know, that somewhere in the world there's a server with a microphone placed outside the window or a little radio antenna listening to every signal that "passes by".

We then proceed with [CloudFlare](https://www.cloudflare.com/) which uses the Entropy Wall, a wall of lava lamps as you can see in [this video](https://www.youtube.com/watch?v=1cUUfMeOijg&ab_channel=TomScott) by Tom Scott. A lava lamp, other than being pretty and colorful, is one of many real world examples of a chaotic system. The physics behind a lava lamp is entirely deterministic but in a chaotic system the rules that change the system's state are strongly dependent on the initial conditions. So, a chaotic system is perfect for this job because it makes really hard to predict the next states and, therefore, the next numbers that are generated from it.

Another fancy idea (which probably inspired the developers of random.org) comes from nothing less than Alan Turing. He once was asked to develop a system to encrypt analog radio communications and he did, of course, but when he needed to use a random key to better encrypt the communication, he decided to rip off the antenna of a radio and use the received signal as the key.

We end up to the hardware RNG of the Linux (and probably many others) kernel. By reading the file `/dev/random` on a Linux system we have access to a stream of random bits generated from *hardware noise* gathered from all devices connected to the system. This *hardware noise* comes from certain phenomena that happen at the microscopic level (involving electrons and transistors) which are either quantum-related (so they are naturally random) or ruled by some unknown or uncomputable formula.

As you may have noticed from these examples, professionals seek non-determinism as the seed for their deterministic RNGs. So, finally I can explain my idea. I thought "where can I find some non-deterministic phenomenon inside each computer?". The atmospheric noise or internet noise idea was already taken so I went to the magic world of parallelism. You may already see where this is going. Everytime someone explains parallelism and/or threads and/or mutual exclusion to a newbie, he/she explains that
> you have no control on the scheduling of threads/processes, you can only control when to start them and when to wait for them to finish

This happens because the scheduler of each OS decides which thread/process to run on which core and for how much time. Although many schedulers may be entirely deterministic (in order to have a reproducible behavior), they work in an environment so chaotic that they seem completely non-deterministic. Just think about all the variables that are involved:
 - how many processes/threads are currently running
 - how many processes/threads are waiting in the queue to be executed
 - I/O operations (with a disk or with the network) that terminate changing the state of a process
 - OS processes with higher priority that wake up to do their job

But also some external factors like:
 - CPU temperature (if in battery-saving mode, the scheduler may decide to reduce workload scheduling less jobs)
 - available free RAM (maybe some process waiting for I/O was transferred on disk on the swap memory and it needs to be reloaded back on memory)
 - sudden interruption of I/O operations (you unplug the USB drive without having properly unmounted it, or the SSD burns because of a hardware error)

All these variables may be predictable and deterministic if considered alone, but together they form a really complicated chaotic system and thus, a good starting point for random number generation.

So I decided to try to build a random number generator based on thread scheduling.

# Implementations
## Version 1.0
The most basic implementation is the classic example of a race condition.

There's a shared variable: an integer initialized to 0. There are two threads which change its value forever. One of the threads increases it while the other one decreases it. This example is used to show the use and meaning of a mutex around that variable.

```c
#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

int main(void) {
    const unsigned int n = 100000;
    int x = 0;

    #pragma omp parallel num_threads(2) default(none) \
    shared(n, x)
    for(unsigned int i=0; i<n; i++) {
        switch(omp_get_thread_num()) {
            case 0:
                x++;
                break;
            case 1:
                x--;
                break;
            default:
                printf("ERROR\n");
                break;
        }
    }

    printf("Final value: %d\n", x);

    return EXIT_SUCCESS;
}
```
This program is technically a random number generator whose generated number is the final value of `x`. The generated number can range anywhere between `-n` and `n` based on the scheduling. However, the resulting distribution is not uniform (but normal/gaussian) because values closer to 0 are more likely to occur. You can think of this like a pair of dices from which you generate numbers as the sum of the two results. The generated numbers range anywhere in the integers between 2 and 12 inclusive, but 2 and 12 have only 1 possible way of being generated while numbers like 6 have many more possibilities. This simple generator works the same way but with a much bigger range.

## Version 2.0
I thought of various ways to improve this RNG. The randomness and chaotic behavior come from the race conditions that occur during execution. So I thought "more race conditions = more non-determinism = more randomness". So I decided to add more threads.

But I cannot have N threads divided in 2 groups: the "increasers" and the "decreasers". I decided to add more possible tasks that the threads can perform, in the form of different formulae. These tasks must:
 - be simple (because they need to be executed fast)
 - not lock themselves in a loop by executing the same task in sequence without race conditions

I need to explain the second point. Operations like `x++`, `x--`, `x*=3`, `x*=(x+1)` are good because they have a *long-enough* period, considering overflow, until they come back to the initial conditions (where "long-enough" means that the other threads in the pool have enough time to wake up and start messing with the value). However, other operations like the following ones aren't good:
 - `x*=2` has a period of 32 (if the value is a common 32-bit integer)
 - `x/=2` takes 32 steps at most to arrive to 0, from where it doesn't move anymore
 - `x^(x-1)`

## Side-effects

# Evaluation
## Distribution
## Performance