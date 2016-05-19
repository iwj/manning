# -*- coding:utf-8 -*-

import random


#抛硬币
counter_front = 0
counter = 0
for i in range(88):
    print "* "*9
    print "第%i次" % (i+1)
    rst = random.randint(0,1)
    print rst
    if rst:
        print "正面"
        counter += 1
        if counter == 3:
            print "达到连续3次正面朝上啦"
            counter_front += 1
    else:
        counter = 0
        print "反面"
print "一共出现了%i次连续3次正面朝上" %counter_front
