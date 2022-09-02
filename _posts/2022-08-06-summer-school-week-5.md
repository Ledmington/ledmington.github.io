---
layout: post
title:  "PRACE Summer School of HPC Blog #5"
summary: "How to (not) use C macros"
author: ledmington
date: '2022-08-06 12:35:00 +0000'
category:
 - blog
 - prace
 - hpc
thumbnail: /assets/img/sohpc-logo.png
keywords: blog, prace, hpc
permalink: /blog/summer-school-week-5/
usemathjax: true
published: false
---

I don't know if you know what a C macro is, so I'm giving you a little explanation.

A [macro](https://gcc.gnu.org/onlinedocs/cpp/Macros.html) is a special kind of **preprocessor directive** and it's a feature of the C language. As far as I know, no other language after C has used again this feature for many reasonable reasons, the first one being that
> Using macros is writing code inside your code.

Like all the other preprocessor directives, macros allows you to control the compiler behavior *while it's compiling your code*, but in an indirect way. Macros are mostly symbols, variables that can be `#define`d usually to tell the compiler to include a certain header file only once, the so-called **include guards**. Other macros are mappings of strings to other strings or functions to other functions. When a compiler encounters a macro, it substitutes every occurrence of that symbol with the (optional) second part. Let's go through some example.

Let's say that you want to quick way to log to the console in your program so you define this macro:
```c
#define LOG printf
```
and now you can use it like this:
```c
LOG("x is %d\n", x);
```
and the compiler will change it to:
```c
printf("x is %d\n", x);
```

This is not a clever way to use macros, since a string like `"I LOVE LOGGING"` would also be modified to `"I LOVE printfGING"`. For this reason, usually a logging macro is deifned as follows:
```c
#define LOG(fmt, ...) printf("[%s]"fmt, get_time(), ...)
```
This macro substitutes every `LOG` to a call to printf and it also adds the current timestamp.

...

## Macro's house of horrors
- macros that map to nothing
- macros that map to macros that map to nothing
- macros that map to macros that map to macros that map to nothing
- macros to include bugfixes or not
- macros that are not refactored to be unique
- code that (in certain combinations) uses undefined macros
- macros that define the same thing twice but for the same purpose
- macros to ask for certain parameters and macros to set them
- macros to get the size of a given (unknown at compile time) data type
- macros to ask for (and I quote) "more parallelism"
- macros to ask for more verbosity only about certain operations or, even worse, only about certain formats
- macros that map to actual function calls (so why did you need the macro anyway?)
- "preamble" macros that map to nothing
- a macro that maps to `stdlib`'s `free`
- a `CONDITIONAL_FREE` macro that deallocates a pointer and sets it to NULL if and only if it is NULL. The problem this macro is solving was already solved with the [C89 standard](http://port70.net/~nsz/c/c89/c89-draft.html#4.10.3.2)

## General code horrors
- six nested levels of `switch` statements, to map to every possible combination of six hyper-parameters, each one with just a single line of code (and the `break;` instruction): the call to a function that performs the same algorithm but with slightly different hard-coded (inner) parameters but with always the same arguments in the same order.
- code wrapped in a `#if 0` that is not at all useful for debugging
- goto statements to handle simple error situation (for example, with no deallocation required)
- goto statements that wrap the whole body of a `for` loop to repeat a certain iteration with the same parameters
- compilation error/warning handling through `#pragma GCC push/pop` directives