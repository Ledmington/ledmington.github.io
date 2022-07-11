---
layout: post
title:  "PRACE Summer School of HPC 2022"
summary: "Developing CUDA in Luxembourg"
author: ledmington
date: '2022-05-13 15:30:00 +0000'
category:
 - hpc
thumbnail: /assets/img/iris.jpg
keywords: prace, hpc
permalink: /blog/summer-school/
usemathjax: true
---

Hi everyone, I've been selected to participate in PRACE's Summer School of HPC 2022!

# What is the PRACE Summer School of HPC?
[PRACE](https://prace-ri.eu/) is a european organization (not created by the EU, as far as I know) whose mission is to connect high-impact scientific and engineering research projects to High-Performance Computing systems.

They also organize a lot of free courses (many remotely, but also on site) about HPC, ranging from deep learning in python to code optimization in Fortran. They also organize many training events during the year and the most important one is of course the [Summer School of HPC](https://summerofhpc.prace-ri.eu/). A certain number (usually between 20 and 40) of students (from undergraduate to master's students) is selected and assigned to some real HPC research projects around Europe.

# The project I'll be working on
It's called "Designing scientific application on GPUs" (you can look it up [here](https://summerofhpc.prace-ri.eu/designing-scientific-applications-on-gpus-2/)) and, as far as I understood it, it consists of translating some known algorithms written in C/C++ into C+CUDA.

I will have a personal desk and access to the IRIS cluster of the University of Luxembourg (the one in the photo). If you take a look over [here](https://hpc.uni.lu/old/systems/iris/), you can see the detailed specs. Since I'll be working with CUDA, I'm actually interested in the "GPGPU accelerators" part:
- 18 nodes, each one with 4 NVIDIA Tesla V100 SXM2 16GB
- 6 nodes, each one with 4 NVIDIA Tesla V100 SXM2 32GB

All of this hardware sums up to 96 GPUs and 1920 GB of integrated memory. Just on the graphics cards!

What is the cost of all this? As of today, 13th May 2022, a single NVIDIA Tesla V100 SXM2 16GB ranges from 6700€ to 8000€. So, to calculate a lower bound we do 6700€ * 96 GPUs = 643'200€. Half a million euros just for GPUs. I love it!

About the CPUs, it seems (unfortunately, the website isn't that clear about processors) that the IRIS cluster has 168 Dell PowerEdge C6320 each one equipped with 28 cores and 128 GB of RAM.

It will be a pleasure to run programs on such a monster.