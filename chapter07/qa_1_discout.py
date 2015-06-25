# -*- coding:utf-8 -*-
"""
低于十给10%折扣
高于十给20%折扣
"""

price = float(raw_input("价格多少"))
if price <= 10:
    print "给10%折扣"
    print price * 0.9
else:
    print "给20%折扣"
    print price * 0.8
