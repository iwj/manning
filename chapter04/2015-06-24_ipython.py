"""
Nothing! Do not view, just command record.
"""
JianWoodeMacBook-Pro:chapter04 Jian$ ipython
Python 2.7.6 (default, Sep  9 2014, 15:04:36)
Type "copyright", "credits" or "license" for more information.

IPython 3.1.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]: float("a")
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-1-1dffa32ffa3b> in <module>()
----> 1 float("a")

ValueError: could not convert string to float: a

In [2]: a = 24

In [3]: b = float(a)

In [4]: a,b
Out[4]: (24, 24.0)

In [5]: a b
  File "<ipython-input-5-7557d2f3a6ad>", line 1
      a b
            ^
            SyntaxError: invalid syntax


            In [6]: a
            Out[6]: 24

            In [7]: b
            Out[7]: 24.0

            In [8]: print ""


            In [9]: print ""


            In [10]: print "float()不会改变原来的值，只是创建一个新值。"
            float()不会改变原来的值，只是创建一个新值。

            In [11]: 0.1+0.2
            Out[11]: 0.30000000000000004

            In [12]: print 0.1+0.2
            0.3

            In [13]: 0.01+0.02
            Out[13]: 0.03

            In [14]: 0.2+0.2
            Out[14]: 0.4

            In [15]: 0.2+0.3
            Out[15]: 0.5

            In [16]: 0.2+0.01
            Out[16]: 0.21000000000000002

            In [17]: print "通常舍入误差都很小，所以不必担心这些误差。"
            通常舍入误差都很小，所以不必担心这些误差。

            In [18]: c = 999.99

            In [19]: d = int(c)

            In [20]: c
            Out[20]: 999.99

            In [21]: d
            Out[21]: 999

            In [22]: print "int()函数总是向下取整，它不会给你最接近的整数。实际上int()函数就是去掉小数部分。"
            int()函数总是向下取整，它不会给你最接近的整数。实际上int()函数就是去掉小数部分。

            In [23]: "今天剪了个毛寸，头皮再也不痒了，人也觉得年轻了。"
            Out[23]: '\xe4\xbb\x8a\xe5\xa4\xa9\xe5\x89\xaa\xe4\xba\x86\xe4\xb8\xaa\xe6\xaf\x9b\xe5\xaf\xb8\xef\xbc\x8c\xe5\xa4\xb4\xe7\x9a\xae\xe5\x86\x8d\xe4\xb9\x9f\xe4\xb8\x8d\xe7\x97\x92\xe4\xba\x86\xef\xbc\x8c\xe4\xba\xba\xe4\xb9\x9f\xe8\xa7\x89\xe5\xbe\x97\xe5\xb9\xb4\xe8\xbd\xbb\xe4\xba\x86\xe3\x80\x82'

            In [24]: e = "20.15"

            In [25]: f = int(e)
            ---------------------------------------------------------------------------
            ValueError                                Traceback (most recent call last)
            <ipython-input-25-20a9433ed325> in <module>()
            ----> 1 f = int(e)

            ValueError: invalid literal for int() with base 10: '20.15'

            In [26]: f = floatt(e)
            ---------------------------------------------------------------------------
            NameError                                 Traceback (most recent call last)
            <ipython-input-26-054e8ef5a060> in <module>()
            ----> 1 f = floatt(e)

            NameError: name 'floatt' is not defined

            In [27]: f = float(e)

            In [28]: e
            Out[28]: '20.15'

            In [29]: f
            Out[29]: 20.15

            In [30]: int(f)
            Out[30]: 20

            In [31]: type(e)
            Out[31]: str

            In [32]: type(f)
            Out[32]: float

            In [33]: print type(e)
            <type 'str'>
