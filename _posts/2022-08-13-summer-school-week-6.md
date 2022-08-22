---
layout: post
title:  "PRACE Summer School of HPC Blog #6"
summary: "Has anybody seen the test results?"
author: ledmington
date: '2022-08-13 12:35:00 +0000'
category:
 - blog
 - prace
 - hpc
thumbnail: /assets/img/sohpc-logo.png
keywords: blog, prace, hpc
permalink: /blog/summer-school-week-6/
usemathjax: true
published: false
---

In the first weeks, when I was looking for papers explaining the theory behind LibRSB, I came across this sentence written by the author:
> ... thanks to many user contributions, the test suite has grown significantly over the years

At that time I thought "wow, this library must be a really good example of test-driven development with all the bugfixes that have been added over the years".
Boy, I really couldn't imagine the real meaning of that sentence. Especially of the word *significantly*.

Later on, I tried to compile the library in order to run some little test programs and the actual tests of the library. I quickly noticed that they were taking a lot of time both on my laptop and on my workstation. That's when I decided to try them on the cluster. After an hour in single-threaded mode, and **fifty thousand** test cases executed, I couldn't see the end. So I started giving more power and more time to the cluster but I still couldn't find the end.

The final configuration used 28 physical cores (no HyperThreading was enabled) divided into 2 CPUs in 2 different machines and it run for 10 hours straight. After 80'000 test cases, the job was killed. Eighty thousand. **EIGHTY THOUSAND!!**

My biggest test suite included 400+ test cases which required at most 6 minutes with minimal RAM usage and single thread mode. So, after a whole week I gave up on trying to run the tests.

Some days later, I found the answer on the [official documentation](http://librsb.sourceforge.net/doc/1.3.0.0/index.html).

> Q: How is correctness checked in the librsb test suite ?
>
> A: Different linear system generators and tester programs are being used to
>    brute-force-test several routines and input combinations as possible.