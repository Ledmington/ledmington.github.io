---
layout: post
title:  "PRACE Summer School of HPC Blog #3"
summary: "First week of implementation"
author: ledmington
date: '2022-07-23 12:35:00 +0000'
category:
 - blog
 - prace
 - hpc
thumbnail: /assets/img/sohpc-logo.png
keywords: blog, prace, hpc
permalink: /blog/summer-school-week-3/
usemathjax: true
---

I spent most of the time this week studying (again) the theory behind the `librsb` library and finding the right place where to start my job.

## Recursive Sparse Blocks
Recursive Sparse Blocks, RSB for short, is an hybrid matrix storage format which uses three different data structures at three different levels to store a sparse matrix:

 - *at the root level*, submatrices/blocks are sorted using the **Z Morton** sorting.
    The Z Morton sorting is a bidimensional sorting that follows the path of a Morton curve, a space-filling curve like the Hilbert's spiral but with the shape of a Z. This feature is used to ensure spatial locality of data in the matrix: each non-zero block is stored in memory really close to its neighbors which it needs to know in order to perform a multiplication.

 - *at the intermediate level*, submatrices/blocks are recursively subdivided into a **Quad-tree** structure.
    A Quad-tree is a really nice data structure that is a specific quaternary tree in which each node represents a portion of a bidimensional space, usually continuous but in our case the matrix coordinate space is discrete. This data structure is optimized for "bidimensional range queries" (the ones like "who are all the points at most far N from me?") which run in $$O(log n)$$ but LibRSB uses it just for better parallelization. Furthermore, the heuristic used to decide whether or not to split a given block involves the size of the largest cache level, so that each block can fit entirely in the cache when processed.

 - *at the leaf level*, each submatrix/block is stored using the standard **COO/CSR/CSC** formats.
    Which one of this formats to use is decided at *allocation time* so, yes, a matrix can have multiple blocks stored in a certain format while others, maybe neighbors, are stored in another format.

## The operations
 - **SpVV**: multiplication between a sparse vector and a dense one
 - **SpMV**: multiplication between a sparse matrix and a dense one
 - **SpMM**: multiplication between a sparse matrix and a dense one or between two sparse matrices
 - **SpSV**: resolution of a linear system in which the equations are expressed as a sparse matrix and the known terms are in the form of a dense vector
 - **SpSM**: resolution of a linear system in which the equations are expressed as a sparse matrix and the known terms are in the form of a dense matrix

## My work
I actually started working on the function `rsb_cuda_mtx_alloc_from_coo_const` which, as you can maybe tell from the name, allocates a matrix in RSB format reading it from one stored as COO. To simplify my job, I am using only `cudaMallocManaged` calls: this way I exploit the CUDA unified memory to write less code.