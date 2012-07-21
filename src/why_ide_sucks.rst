Why IDE sucks
#############

.. TODO: which IDE can be added?

:status: draft

This article is about productivity, as a conclusion of many years of
tinkering and trying every possible thing.

Here below a list of arguments that make every IDE suck:


Designed with a specific language in mind
=========================================

Every IDE is designed with a particular language in mind.  This is not
in general a bad thing, but unless you plan to use *one* and *only
one* programming language, you will experience that the quality of the
plugins for other languages will not be the same.

In plus it takes years before reaching a plugin with a decent quality
for a new language, which leads to the.


Slow and extremely memory hungry
================================

Even on a very fast machine, firing up an IDE takes ages, and
allocates insane amount of memory.  You might say that it's not a
problem, we have power and we have a lot of cheap memory, so why
bother.

But suppose you're working with a netbook, working with that same IDE
is not so much fun anymore, and you end up with your good old
text-editor to get some work done.


Hard to extend or customise
===========================

As developers we have an incredible advantage over other
professionals, we are probably the only one that can create the tools
we are using for our job.

A formula1 pilot doesn't build its car, a carpenter doesn't fabricate
its hammers and so on.  Even more extremely, we can create our own
tools in the same language that we use to do the real job, imagine if
it would be possible to build a hammer just with *another hammer*.

This opportunity gives the tremendous power to customise every tool to
our specific needs and taste.  The problem with IDEs in this case is
that they are extremely hard to customise.

.. TODO: check the link
.. _`emacs configuration`: http://github.com/AndreaCrotti/Emacs-configuration.git

.. TODO: add a simple example about customisation in emacs


When they break you're screwed
==============================

.. _linux_as_ide: http://blog.sanctum.geek.nz/unix-as-ide-introduction/


Complex and not portable configuration
======================================

For my experience it's from very annoying to almost impossible to try
to port the same configuration on different machines.  IDEs often
store all the settings in some thousands sparse xml files, which make
them extremely hard to locate and to understand.


Conclusion
==========


If you are like me, and you always want to know what is going on your
machine.

I'm not saying that IDEs should never been used, on the contrary they
can be very useful.  To me for example one case where I would prefer
an IDE is if I have to implement something quickly in a complex
technology that I don't particularly care about (Java for example).

In that case trying to set up Emacs to get a good configuration
