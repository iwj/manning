# -*- coding:utf-8 -*-
"""
华氏度转摄氏度
"""

degree_F = int(input("input degree Fahrenheit = "))
#2015-06-24 Update: 将输入的温度int()
print "degree_f =",degree_F
print "Celsius degree =", 5.0/9*(degree_F-32)
"""
BUG 整除的原因，导致5/9等于0，导致整个结果衡等于0
把5改成5.0
"""
