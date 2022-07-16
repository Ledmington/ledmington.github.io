---
layout: post
title:  "PRACE Summer School of HPC Blog #1"
summary: "Remote training week"
author: ledmington
date: '2022-07-09 10:50:00 +0000'
category:
 - blog
 - prace
 - hpc
thumbnail: /assets/img/sohpc-logo.png
keywords: blog, prace, hpc
permalink: /blog/summer-school-week-1/
usemathjax: true
---

# The training week
The first week of the Summer School of HPC 2022 is supposed to be for training, teaching the very basics of MPI, OpenMP, CUDA and OpenACC. There's actually very little to be talking about. I already knew almost everything they taught us, except for some variants of the send and receive operations in MPI. I learnt the difference between "asynchronous" and "non-blocking" by using the `MPI_Issend` function which sends a message to another process synchronously and without blocking the current process. As far as I understood it, this function doesn't return until the other process has started to receive the message and the send operation is performed in a separated thread in order to avoid blocking the main process.

Apart from this, I was actually interested in OpenACC and OpenMP GPU offloading because I've never heard of them before this training week. OpenACC is, shortly, "the same thing that OpenMP is for CPUs, but for GPUs". Formally, OpenACC is a declarative directive-based language for GPU programming. Lastly, OpenMP GPU offloading is a set of special OpenMP directives (like `kernels` and `teams`) designed to specify declaratively the GPU computation process. You can specify which variables are supposed to be copied to and from the GPU and which ones are visible outside threads or thread blocks (or, as they call it, teams).

Unfortunately, they taught us nothing about multi-GPU support.

# My project
I've finally understood my project, this week, while talking with my mentor Mr. [Ezhilmathi Krishnasamy](https://wwwen.uni.lu/snt/people/ezhilmathi_krishnasamy). I will have to implement a CUDA version of the [`librsb`](http://librsb.sourceforge.net/) library. The LibRSB library is a "shared memory parallel sparse matrix computations library for the Recursive Sparse Blocks format" which is currently implemented in C, Fortran and C++ with OpenMP's CPU parallelism and has a binding for Julia and Python. It also implements the Sparse BLAS standard. So, my job will be to allow it to use NVIDIA GPUs but it can't just be an API binding, I (probably) need to implement the core functions from scratch.

I will try to write a post at the end of each week until the end of August, so stay tuned and don't miss the next one!