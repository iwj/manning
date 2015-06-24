"""
Nothing! Do not view, just command record.
"""
JianWoodeMacBook-Pro:chapter05 Jian$ ipython
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: name = raw_input("woohoo:")
woohoo:hoowoo

In [2]: name
Out[2]: 'hoowoo'

In [3]: name = raw_input("woohoo:"),
woohoo:yahoo

In [4]: name
Out[4]: ('yahoo',)

In [5]: type(name)
Out[5]: tuple

In [6]: number = float(raw_input)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-0cd77555f050> in <module>()
----> 1 number = float(raw_input)

TypeError: float() argument must be a string or a number

In [7]: number = float(raw_input())
2015

In [8]: number = float(raw_input())
0.1

In [9]: number = float(raw_input())
0.2

In [10]: number = float(raw_input())
0.3

In [11]: number = float(raw_input())
0.1+0.2
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-11-12331221f0cc> in <module>()
----> 1 number = float(raw_input())

ValueError: invalid literal for float(): 0.1+0.2

In [12]: number = float(raw_input())
(0.1+0.2)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-12-12331221f0cc> in <module>()
----> 1 number = float(raw_input())

ValueError: could not convert string to float: (0.1+0.2)

In [13]: 0.1 + 0.2
Out[13]: 0.30000000000000004

In [14]: b = 0.1 + 0.2

In [15]: number = float(raw_input())
b
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-15-12331221f0cc> in <module>()
----> 1 number = float(raw_input())

ValueError: could not convert string to float: b

In [16]: type(b)
Out[16]: float

In [17]: "Oops raw_input()必定会将输入的内容加上“”，所以必定是str"
Out[17]: 'Oops raw_input()\xe5\xbf\x85\xe5\xae\x9a\xe4\xbc\x9a\xe5\xb0\x86\xe8\xbe\x93\xe5\x85\xa5\xe7\x9a\x84\xe5\x86\x85\xe5\xae\xb9\xe5\x8a\xa0\xe4\xb8\x8a\xe2\x80\x9c\xe2\x80\x9d\xef\xbc\x8c\xe6\x89\x80\xe4\xbb\xa5\xe5\xbf\x85\xe5\xae\x9a\xe6\x98\xafstr'
