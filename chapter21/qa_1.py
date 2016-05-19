# -*- coding:utf-8 -*-

print "What is",
print "your name."

print "* "*8
user_name = raw_input("Your name:")
user_age = raw_input("Your age:")
user_fav = raw_input("What color you like:")
print "Your nam is",user_name,"you are",user_age,"and you like",user_fav,"."

print "* "*8
for looper in range(1, 11):
    print looper,"\ttimes 8 =",looper*8


print "* "*8
print "计算分母为8的所有分数，显示3位小数"
for i in range(1,16):
    i_result = i/8.0
    print "%i/8=%.3f" %(i, i_result)
