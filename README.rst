strings
=============

Python strings for humans.

Usage:

.. code-block:: python

    >>> from strings import string
    >>> s = string("Hello, World")
    >>> s
    'Hello, World'
    >>> s.len()
    12
    >>> s.length
    12
    >>> s.size
    12
    >>> s + ", What?"
    Traceback (most recent call last):
      File "strings.py", line 27, in <module>
        x = s.add(", world")
      File "strings.py", line 20, in add
        return self + string(value)
      File "strings.py", line 23, in __add__
        raise NotImplementedError("Use add instead")
    NotImplementedError: Use add instead
    >>> s.add(", What?")
    'Hello, World, What?'
    
Background
-----------

Inspired by an April Fool's Day joke.