"""
Nothing! Do not view, just command record.
"""
JianWoodeMacBook-Pro:chapter03 Jian$ ipython
priPython 2.7.6 (default, Sep  9 2014, 15:04:36)
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: print 8-4
4

In [2]: print 8-3
5

In [3]: print 6/3
2

In [4]: print 6/4
1

In [5]: print 6.0/4
1.5

In [6]: print 6/4.0
1.5

In [7]: "apple"+"a"
Out[7]: 'applea'

In [8]: "apple"-"a"
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-5563ead86896> in <module>()
----> 1 "apple"-"a"

TypeError: unsupported operand type(s) for -: 'str' and 'str'

In [9]: print 3 * 3 * 3 * 3 * 3
243

In [10]: print 3**5
243

In [11]: 3^2
Out[11]: 1

In [12]: 3^3
Out[12]: 0

In [13]: 3^4
Out[13]: 7

In [14]: 7－－
  File "<ipython-input-14-0fc99d5d365a>", line 1
      7－－
           ^
           SyntaxError: invalid syntax


           In [15]: 7--
             File "<ipython-input-15-bad8b8e483d2>", line 1
                 7--
                        ^
                        SyntaxError: invalid syntax


                        In [16]: 7 -= 1
                          File "<ipython-input-16-99cdc6594321>", line 1
                              7 -= 1
                              SyntaxError: can't assign to literal


                              In [17]: print 7-= 1
                                File "<ipython-input-17-a2afc3acc823>", line 1
                                    print 7-= 1
                                                ^
                                                SyntaxError: invalid syntax


                                                In [18]: number = 7

                                                In [19]: number -= 1

                                                In [20]: number
                                                Out[20]: 6

                                                In [21]: number += 11

                                                In [22]: number
                                                Out[22]: 17

                                                In [23]: print 23467892345678 * 345673456743567
                                                8112227469616411230966753426

                                                In [24]: print 23.467892345678 * 34.5673456743567
                                                811.222746962

                                                In [25]: print 233456789.467892345678 * 3467834.5673456743567
                                                8.09589524498e+14

                                                In [26]: 3.8e16
                                                Out[26]: 3.8e+16

                                                In [27]: print 3.8e16
                                                3.8e+16

                                                In [28]: type(3.8e16)
                                                Out[28]: float

                                                In [29]: 1.7e7
                                                Out[29]: 17000000.0
