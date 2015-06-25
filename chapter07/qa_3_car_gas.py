# -*- coding:utf-8 -*-

volume = float(raw_input("你的油箱可以装多少L汽油？程序自动保留5L的缓冲区，以防油表不准。"))
status = float(raw_input("目前余量占多少百分比？仅需输入数字即可，无需输入百分号")) * 1e-2
print status
perliter_route = float(raw_input("每升可以行驶多少千米？"))

route = ( volume * status - 5 ) * perliter_route
print route

if route >= 200:
    if int(route) ==200:
        #BUG 如果这样写 route == 200 则判断为False，当加上int()之后就正常，令人诧异啊
        print "刚刚好可以行驶到下一个加油站"
    else:
        print "燃料充足，可以到下一个加油站再加油"

else:
    print "加油吧，司机大哥。"
