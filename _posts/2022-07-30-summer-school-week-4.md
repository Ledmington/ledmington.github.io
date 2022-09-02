---
layout: post
title:  "PRACE Summer School of HPC Blog #4"
summary: "From great efficiency, comes great unreadability"
author: ledmington
date: '2022-07-30 12:35:00 +0000'
category:
 - blog
 - prace
 - hpc
thumbnail: /assets/img/sohpc-logo.png
keywords: blog, prace, hpc
permalink: /blog/summer-school-week-4/
usemathjax: true
---

I think I finally got my head around what the LibRSB library is really doing and how it's doing it.

Before telling you the strangest (but absolutely justified) operations I've seen in this library, I would like to ask you some questions in order to better understand later.

You are working in C. Let's say that you want to implement the matrix multiplication algorithm and you want to implement it in the most general version, obviously. So, your algorithm presumably would require (at least) 5 parameters:
 - a matrix for the result, $$Z$$
 - the two input matrices, $$X$$ and $$Y$$
 - two scalars to scale matrices, $$\alpha$$ and $$\beta$$

and it would perform this operation:
$$Z \leftarrow \alpha \cdot X \times \beta \cdot Y$$

My question is the following:
> How many early exit conditions and corner cases are there?

These are the ones that I've found:
 1. if $$\alpha$$ is 1, the multiplication $$\alpha \cdot X$$ can be skipped since it doesn't change the final result. The same applies to $$\beta \cdot Y$$.
 1. if $$X$$ is simmetric, the algorithm can be improved to iterate only half of the matrix. The same applies to $$Y$$.
 1. if $$X$$ is triangular, the algorithm can skip a half of the multiplications. The same applies to $$Y$$.
 1. if $$X$$ is diagonal, the algorithm can skip even more multiplications. The same applies to $$Y$$.
 1. if $$X$$ is the identity matrix, the whole multiplication algorithm can be skipped. The same applies to $$Y$$.
 1. if $$X$$ and $$Z$$ are different matrices, the algorithm can directly store the result inside $$Z$$ without a temporary matrix. The same applies to $$Y$$.

Now let's consider the combinations of these cases. The number 1 is independent from all the others but it means that we should have one check on $$\alpha$$ and one on $$\beta$$. The points 2-3-4-5 are not entirely independent from each other, so we could consider them as a single parameter with 5 possible values: simmetric, triangular, diagonal, identity, none-of-the-above. Another parameter also for $$Y$$. Lastly, the point 6 can be translated in a single parameter with 2 possible values: either at least one of $$X$$ and $$Y$$ is $$Z$$, or it's not. Already from these simple considerations, we obtained $$2 \cdot 2 \cdot 5 \cdot 5 \cdot 2 = 200$$ possible combinations of parameters. This means that, in order to obatin maximum efficiency, we should implement 200 times the same algorithm but with minor modifications because filling with `if`s the generic version is surely better for code readability but it's not optimized for efficiency.

This is the line of reasoning that LibRSB follows. In the case of the matrix multiplication algorithm, it was true for the only one that I've worked on (SpMV) which was one of 5 different algorithms. And this one had 6 different parameters to be combined resulting in a 50K+ lines of C code.

There are many other little things that this library does and this one was just the pinnacle that stood in my memory until now. The examples that come to my mind right now are:
- all the computation and choices that LibRSB makes only to decide what format to use for each allocated submatrix like the estimated size to check if it's going to fit entirely in the L3 cache
- the computation performed just to decide how many threads to use to perform a parallel recursive allocation
- the computation to decide how many threads to use to copy a sparse matrix from format X to format Y
- which format is better suited for the current configuration (the current machine) of available memory, number of threads and cache hierarchy