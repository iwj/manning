# -*- coding:utf-8 -*-
"""
华氏度转摄氏度
"""

degree_F = input("input degree Fahrenheit = ")
print "Celsius degree =", 5.0/9*(degree_F-32)
"""
BUG 整除的原因，导致5/9等于0，导致整个结果衡等于0
把5改成5.0
"""
