---
layout: post
title:  "Most liked features"
summary: "As of March 2022"
author: ledmington
date: '2022-03-30 23:05:00 +0000'
category: blog
thumbnail: /assets/img/features.gif
keywords: blog, features
permalink: /blog/most-liked-features/
usemathjax: true
---

This is a personal list of the best features I've found so far in my (little) experience with software development. No preference-based order intended.

# texdoc
As a developer, you should have already heard of **LaTeX**. I'm not explaining what it does, but I personally find it more fun than other document editors because it's actually code that you write to *declare* what you want in your document.

LaTeX itself has its faults, for example the excessively verbose syntax. That's why this section isn't about the whole ecosystem but a small part of it. A LaTeX document needs many packages to compile because each one of those does a very specific thing: the package `algorithm2e` is used to write pseudocode, the package `tikz` to draw custom graphs and charts and so on. Each package has its own set of commands, each one with its set of allowed parameters, all described in its documentation. That's where `texdoc` comes to the rescue.

The `texdoc` command is added whenever you install locally a LaTeX distribution (worked both with MikTeX and TeXlive) and has a very very simple syntax:
```
texdoc <package-name>
```
opens the pdf of the documentation of the given package.

I find it absolutely wonderful and it already helped me many times. It comes with a normal distribution, simple syntax and gets the job done fast. What else can you ask for?

Note: AFAIK it only looks for a directory with the name of the given package and opens the pdf inside that folder. Unfortunately, it doesn't compile the documentation (that could be written in LaTeX) with a lazy style, adn maybe that's the reason why the TeXlive distro weighs around 4 GBs.

# Visual Studio Code Web mode
This section's title is a spoiler. I actually don't know how this thing is called but I'll stick with this name. Maybe you don't know about this and can discover it yourself by clicking [here](https://vscode.dev).

Oh yes, that's VS Code that runs entirely in your browser (the first time you use it it can be really slow). That's absolutely useful when you need to work on some new pc in a place different from your usual one. (BTW, the link is **vscode.dev**)

It has its (obvious) down-sides: plugins.

Not all plugins can be installed while in web mode (or can be installed but can't work). A notable example is the Jupyter Notebook plugin. Another is the Python plugin, that can only perform syntax highlighting and code linting while in web mode.

## VS Code in GitHub
This one is actually considered a part of the one above, a DLC. I think this feature is born because Microsoft bought GitHub. Apparently, if you open any repository on GitHub and press `.` (dot), your browser will open Visual Studio Code in Web mode inside that repository.

This may seem like an awkward way to work, but it can be actually useful when, for example, you can't use your usual computer to work and you need to apply some quick changes. I haven't told you the best part. VS Code has always pre-installed a plugin to use git, but since you are working on the remote version of the repo, you don't need to push your commits. I discovered this feature by chance when I was learning how to use GitHub Actions workflows by (a painful lot of) trial and error. This was definitely a game changer.

# Automatic plugin finding based on file type
Yes, I'm talking about you two, **Intellij** and **Visual Studio Code**! (Is it so obvious that I like VS Code?)

There's not so much to say about this. I absolutely love the *comfort* about the whole "would you like to install the recommended plugin for this file?" thing. As an added bonus, many of those plugins are hot-swappable, they work right away and can be replaced without restarting the whole program.

If you think about it, it isn't a complicated feature, especially if each plugin has to declare the file types that it works with. A part from this, apaprently many other editors and IDEs don't implement this feature for whatever reason and it's a bit disappointing (maybe because it can be annoying sometimes).

# git bisect
Did you find a bug in your code?

Is your `git log` longer than the Bible?

Your tests can't catch the bug?

Your debugger doesn't see the bug?

When you add some `printf`s around, the bug disappears?

Fear not, developer, because **git bisect** is here to help you!

First of all, some theory. If you found a bug in your branch, it means that sometime in the past a commit introduced it in your code. Now imagine to replace each commit in your branch that hasn't the bug with a `0` and each bugged commit with a `1`. Now you have a very long list of `0`s followed by a (hopefully not) very long list of `1`s, so it is sorted.

As a wise man once said,

> When you have a sorted search space, you can perform a binary search.

At this point, finding the first commit that introduced the bug is just a matter of binary search through the commits of your branch.

I'm not going to make a full guide on how to use it, but it goes around three commands:
 - `git bisect start` to start the **bisect mode** (remember to clean up your working tree before starting)
 - `git bisect good` to tell git that the current commit has not yet the bug (it is in the `0` part)
 - `git bisect bad` to tell git that the current commit has the bug (it is in the `1` bug)

The fact that it uses a binary search is the key to making it a *usable* feature, because even with thousands of commits, `bit bisect` is going to find the right one in 10 (or a few more) checkouts.

However, the questions at the beginning are an example of how specific the situation needs to be in order to use this feature. Up to now, in the 3 years that I've been actively using git, I used `git bisect` just 3 times when two of these conditions were met:
 - the code to debug was not mine
 - the bugged branch had more than 200 commits
 - I could not find a way to automate the test

Note: remember to `git bisect reset` when you're done, otherwise git will start doing weird things with your files.