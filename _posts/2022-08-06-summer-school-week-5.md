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
---

I don't know if you know what a C macro is, so I'm giving you a little explanation.

A [macro](https://gcc.gnu.org/onlinedocs/cpp/Macros.html) is a special kind of **preprocessor directive** and it's a feature of the C language. As far as I know, no other language after C has used again this feature for many reasonable reasons, the first one being that
> Using macros is writing code inside your code.

But they are useful and some libraries (like [minunit](https://jera.com/techinfo/jtns/jtn002)) use only macros to create **0 memory** libraries.

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

This is not a clever way to use macros, since a string like `"I LOVE LOGGING"` would also be modified to `"I LOVE printfGING"`. For this reason, usually a logging macro is defined as follows:
```c
#define LOG(fmt, ...) printf("[%s]"fmt, get_time(), ...)
```
This macro substitutes every `LOG` to a call to `printf` and it also adds the current timestamp.

These ones are the macros that can be used inside the code, because they have some behavior. Other macros, commonly defined as **symbols** are "macros that map to nothing" and are usually used to tell the compiler that a certain library is already included or that the machine is using a certain library. For example, the *include guards*
```c
#ifndef MY_LIBRARY_INCLUDED
#define MY_LIBRARY_INCLUDED
...
#endif
```
assure you that a certain file will not be included twice. Another common example is the function that retrieves the current time because C has a clock in the standard library with millisecond precision, but if you want more precision you have to use OS-specific functions. It happened to me only once to write code really similar to the one below: same function API but different implementation based on the OS you are compiling on.
```c
#if defined(_WIN32)
#include <Windows.h>
long get_time() {
    LARGE_INTEGER Frequency, tm;

    QueryPerformanceFrequency(&Frequency); 
    QueryPerformanceFrequency(&tm); 

    tm.QuadPart *= 1000000;
    tm.QuadPart /= Frequency.QuadPart;

    return tm.QuadPart;
}
#elif defined(__linux__)
#include <time.h>
long get_time() {
    struct timespec tm;
    clock_gettime(CLOCK_MONOTONIC, &tm);
    return (tm.tv_sec * 1000000) + (tm.tv_nsec / 1000);
}
#endif
```

These symbols cannot be used inside your code like so
```c
#define WANT_VERBOSE_LOGS
if(WANT_VERBOSE_LOGS) {
    printf("log...\n");
}
```
because this code won't compile.

Now that I've given you more than enough theory, let's go on with the errors and horrors (pun not intended) I found inside the LibRSB source code.

## Macro's house of horrors
This section will cover only the horrors about macros since they were the most common.

##### Symbols used inside the code
This is a compilation error which has been avoided only because of some lucky combination of other macros.

##### Macros that map to symbols, still used inside the code
This was unexpected and worse than the first one.

##### Macros that map to macros that map to symbols used inside the code
I consider this as a joke to the programmer, at this point. You can imagine the frustration of trying to understand this obscure code (thousands of lines of C code), so you follow a macro declaration/mapping and, after two or three "jumps", you end up in a symbol which messes up the compilation.

##### Macros to include bugfixes or not
As a developer, I understand the issues with retrocompatibility but we are talking about a numerical library. A numerical library needs to be correct, the *most correct you can get* so, why the hell should someone want to include a bug in his library?!?

##### Macros that are not refactored to be unique
There were some macros (really few, luckily) who had the same name, with a "2" or a "3" after it, which did the same thing in the same functions. If I remember correctly, there was something like `RSB_SUBDIVISION` and `RSB_SUBDIVISION2`.

##### Code that (in certain combinations of other macros) uses undefined macros
I'm not joking. Code that used undefined macros. Not preprocessor directives, **actual code!!!** I don't need to explain any further.

##### Macros that define the same thing twice but for the same purpose
Two different macros (slightly different names) for logging the contents of an array which mapped to the same code.

##### Macros to ask for certain parameters and macros to set them
If you ever used MPI with C, you should be familiar with functions that require a lot of parameters. LibRSB has a lot of them and many times they don't change those parameters, they just pass them around, for example: a pointer to the variable with the error code, the length of the given arrays, the pointer to the global session handle and so on. Since it was boring and slow to always type those parameters, this library has multiple macros, also used inside function declarations, which map to a list of comma-separated arguments with type and stuff. It may be useful in some cases, but you need to use it very carefully otherwise your code will become pretty obscure pretty quickly.

##### Macros to get the size of a given data type (unknown at compile time)
For some reason, unknown to me, there was the `RSB_SIZEOF` macro which was a chain of 4 `if` statements (and one final `else`) to check if the given type was known and in a defined enumeration and, if so, call the proper `sizeof`. I was very surprised to have found this kind of code inside a library so efficiency-centered. Every C programmer knows that, when you need to perform a lot of equality checks, a `switch` statement is faster than a `if-else` chain.

##### Macros to ask for (and I quote) "more parallelism"
I think that, if you give the user a choice about how much "parallelism" (number of threads which determines a slightly different algorithm) he wants, you have done a bad job at using OpenMP in your code.

##### Macros to ask for more verbosity only about certain operations or, even worse, only about certain formats
I can understand this one because the library was huge (400'000+ lines of code divided in 1'000+ files) and you simply could not log everything during a debugging session (or maybe you could if you had designed everything in a simpler way but nevermind). Nevertheless, it was really ugly to see all these `RSB_DEBUG_XXXXXXXX` macros all over the place.

##### Macros that map to actual function calls
So why did you need the macro?

To be clear, I don't mean a macro with default arguments, I actually mean just using a different name to call a certain function and pass it the same parameters.

##### "Preamble" macros that map to nothing
In some cases, it may be useful to have a "preamble" macro (as I call it, I don't know if there's a proper name) which is a macro that sets the proper values to some global variables or locks some resources or opens the log file. I personally don't like it because you can always create a function called `XXX_init` that *initializes everything* (and LibRSB had it) but I can understand its utility. The only problem is that this macro was defined as a symbol, it mapped to nothing, thus it was useless.

##### A macro that maps to `stdlib`'s `free`
Why? Why a macro? Why not a proper function? I understand that the library is heavily efficiency-centered but this does not affect performance positively (nor negatively).

##### The `RSB_CONDITIONAL_FREE` macro
The `RSB_CONDITIONAL_FREE` macro deallocates a pointer and sets it to NULL if and only if it is NULL. The problem this macro is solving was already solved with the [C89 standard](http://port70.net/~nsz/c/c89/c89-draft.html#4.10.3.2), so not only it is useless, it would have been useless 30 years ago, too.

## General code horrors
This section will cover all the other non-macro-related horrors.

##### Six nested levels of `switch` statements
I explained this idea in the [previous post](../summer-school-week-4/).

This was needed to map every possible combination of six hyper-parameters, each one with just a single line of code (and the `break;` instruction): the call to a function that performs the same algorithm but with slightly different hard-coded (inner) parameters but with always the same arguments in the same order.

##### Code wrapped in a `#if 0` that is not at all useful for debugging
This was straight up **dead code**. Dead code inside every single file, for 3 consecutive releases.

##### `goto` statements to handle simple error situation
Inside some functions, some arrays needed to be deallocated but only if they were dynamically allocated in the first place, to avoid a deallocation error. The function body looked something like this:
```c
void deallocation_function(void *array_ptr, ...) {
    if (array_ptr is on the stack) goto end;

    free(array_ptr);
    
    // code

    end:
}
```

I simply would have written this function like this:
```c
void deallocation_function(void *array_ptr, ...) {
    if (array_ptr is on the stack) return;

    free(array_ptr);
    
    // code
}
```

##### `goto` statements that wrap the whole body of a `for` loop to repeat a certain iteration with the same parameters
This was inside a `#pragma omp parallel for` section. Let me show you more clearly what I mean.
```c
#pragma omp parallel for
for (...; ...; ...) {
    again:
    
    // code

    if ( <condition> ) goto again;
}
```
The condition of the `if` statements was about handling some extra values inside the array used by the threads. I still can't understand why this should have been better than a normal (serial) second for loop like when you're handling leftover elements with SIMD instructions.

##### Compilation error/warning handling through `#pragma GCC push/pop` directives
I never knew about this feature and apparently it is compiler-dependent. Since preprocessor directives tell the compiler what to do during compilation, apparently, you can also tell it to **ignore errors** and, much worse, to **show them where they aren't**. Maybe it's just a big misunderstanding by me, but if I understood it correctly, you could ingore errors during compilation. The only use case scenario I came up with is a rare case in which you need to include a library that, for some obscure reason, is available with different names even on the same OS. So, in order to be sure to have it included, you have to try to include it and then the `#include` directive may fail. In that case, you ignore the error and try to include it with the other name. If it still fails, then you can output an "include error".

Pretty ugly feature, I might say, I will certainly never use it.