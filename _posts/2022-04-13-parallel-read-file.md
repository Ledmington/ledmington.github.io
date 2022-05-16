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
published: false
---

# The problem
The problem is as simple as this question: **Is it possible to read a file in parallel?**
While it may seem really trivial, one you start thinking about the way a hard drive (or an SSD) works a lot of doubts start to rise.

For simplicity, we generate a file with random integers and we want to find the minimum of them.

# The solutions
## Reading serially
## Partition (logically) the file with pointers
## Read different copies at different locations
## Split in physical parts