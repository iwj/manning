"""
Nothing! Do not view, just command record.
"""
JianWoodeMacBook-Pro:chapter07 Jian$ ipython
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: age = 20

In [2]: 18 < age < 22
Out[2]: True

In [3]: age > 0
Out[3]: True

In [4]: age > 0 and False
Out[4]: False

In [5]: age > 0 or False
Out[5]: True

In [6]: not age > 0
Out[6]: False

In [7]: age > 0 and age > 2
Out[7]: True

In [8]: age > 0 and age > 30
Out[8]: False

In [9]: age > 0 and age > 30 or age <200
Out[9]: True

In [10]: age > 30 or age <200
Out[10]: True

In [11]: answer = "q"

In [12]: if answer == "Q" or answer == "q":
       ....:     print "You typed a 'Q'."
          ....:
              You typed a 'Q'.

              In [13]: answer = "Q"

              In [14]: if answer == "Q" or answer == "q":
                      print "You typed a 'Q'."
                         ....:
                             You typed a 'Q'.
