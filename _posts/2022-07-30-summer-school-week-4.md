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
published: false
---

Talk about:
- all the computation and choices that LibRSB makes only to decide what format to use for each allocated block
- all the nested switch statements just to decide which one of the hundreds of specific implementations to use
- how many threads is better to use to perform a recursive allocation
- how many threads is better to use to copy a sparse matrix from format X to format Y
- which format is better suited for the current configuration of available memory, number of threads and cache hierarchy
- storing flags for everything inside a `rsb_mtx_t` structure just to cache informations like: symmetry, "diagonality", "triangularity" and others