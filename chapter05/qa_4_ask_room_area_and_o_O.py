# -*- coding:utf-8 -*-
"""
询问房间尺寸，再计算覆盖房间需要多少地毯
再换算成平方尺
询问每平方尺单价，再计算总价格
"""

length = float(raw_input("你的房间长："))
width = raw_input("你的房间宽：")
print "你的房间是这么多平方米：",length * float(width)
print "你的房间是这么多平方尺：",length * float(width) * 9
unit_price = float(raw_input("每平方尺地毯多少钱($)："))
print "总价：",length * float(width) * 9 * unit_price, "dollars"
