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
for i in range(1,13):
    print i, "\t", i**2, "\t", i**3, "\t", i**4
for i in range(9):
    for j in range(i+1):
#        print "%i ×", i+1,"=",(j+1)*(i+1),"\t",
#        print "%i * %i = %i " %i %i %i
#        print "%i lalala %i" %i, j
        print "暂无"
    print

printStar()
print "在字符串中插入变量："
name = "Jian Woo"
print "My name is", name, "and I wrote this book."

printStar()
print "分解字符串"
name_string  = "Bob,Mary,Tom,Jerry,Hyllen,Cindy,Fish,Joe,Grace"
print "原来字符串：",name_string,"\n分解后："
names = name_string.split(",")
print names
print "单独输出："
for name_one in names:
    print name_one

printStar()
print "join方法："
word_list = ["My","name","is","Warren"]
long_string = " ".join(word_list)
print long_string

printStar()
print "寻找字符串中的关键字："
name_find = "Frankismybrother."
print name_find
re_a = name_find.startswith("Frank")
re_b = name_find.startswith("Frk")
print "startswwich RESULT:",re_a, re_b
re_c = name_find.endswith(".")
re_d = name_find.endswith("ther.")
re_f = name_find.endswith("the")
print "endswich RESULT:", re_c, re_d, re_f
printStar()
print "使用in 和 index查找:"
string_in = "lalalala 657 Maple Lane"
print string_in
if "Map" in string_in:
    print "Find Map in the string!"
    map_index = string_in.index("Map")
    print "Position is", map_index

if "aple L" in string_in:
    print "find 'aple L' in string_in!"
    aple_index = string_in.index("aple L")
    print "Position is", aple_index

printStar()
print "改变大小写Upper() lower()"
string_big_small = "Apple"
string_goo = "google"
print "origin string is", string_big_small, string_goo
string_bs = string_big_small.lower()
string_GOO = string_goo.upper()
print "RESULT:", string_bs, string_GOO
