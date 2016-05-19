# -*- coding:utf-8 -*-

import random


totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1000):
    dice_total = random.randint(0, 15)
    totals[dice_total] += 1

for i in range(0, 16):
    print "* "*8
    print i
    print totals[i]
    print "total", i, "came up", totals[i], "times"
#
# for i in range(999):
#     print random.randint(0, 5)
# 经测试，randint是取得到两个参数的。 而range则是去得到前面一个参数，取到后面的参数－1位置
