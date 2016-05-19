# -*- coding:utf-8 -*-

#两个6面的骰子
import random


totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(999):
    rst_1 = random.randint(1, 6)
    rst_2 = random.randint(1, 6)
    totals[rst_1+rst_2] += 1

# print "两个骰子相加："
print "\t和\t\t次数\t\t百分比"
all_mark = 0
for i in range(2, 13):
    all_mark += totals[i]
# 使用较大的次数（9999999次），结果的百分比趋于一组稳定的数据（固定的数据）
# 	和		次数		百分比
# total 2 	came up 277523 	times	0.03
# total 3 	came up 555878 	times	0.06
# total 4 	came up 833247 	times	0.08
# total 5 	came up 1111615 times	0.11
# total 6 	came up 1388296 times	0.14
# total 7 	came up 1667718 times	0.17
# total 8 	came up 1388459 times	0.14
# total 9 	came up 1109825 times	0.11
# total 10 	came up 832719 	times	0.08
# total 11 	came up 556794 	times	0.06
# total 12 	came up 277925 	times	0.03
for i in range(2, 13):
    # 2 - 12 因为两个骰子，最少2，最多12
    # print "* "*8
    # print i
    # print totals[i]

    print "total", i, "\tcame up", totals[i], "\ttimes\t%.2f"%(totals[i]/float(all_mark))
#
# for i in range(999):
#     print random.randint(0, 5)
# 经测试，randint是取得到两个参数的。 而range则是去得到前面一个参数，取到后面的参数－1位置
