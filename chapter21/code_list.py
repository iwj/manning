# -*- coding:utf-8 -*-


def printStar():
    print "* " * 10

printStar()
print "未加符号："
print "Hi"
print "There"

printStar()
print "加逗号："
print "Hi",
print "There"

printStar()
print "用加号："
print "Hi" + "There"

printStar()
print "中间空一行："
print "Hi"
print 
print "There"

printStar()
print "使用\\符："
print "Hi \\ There"
print "Hi\nThere "

printStar()
print "水平制表符："
print "数字\t平方\t立方\t四次方"
for i in range(1,11):
    print i, "\t", i**2, "\t", i**3, "\t", i**4
for i in range(9):
    for j in range(i+1):
#        print "%i ×", i+1,"=",(j+1)*(i+1),"\t",
#        print "%i * %i = %i " %i %i %i
        print "%i lalala %i" %i, j
    print

printStar()
print "在字符串中插入变量："
name = "Jian Woo"
print "My name is", name, "and I wrote this book."
