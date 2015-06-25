# -*- coding:utf-8 -*-
"""
姓名
门牌号地址街道
城市省
邮编
"""

import easygui


easygui.msgbox("信封")
name = easygui.enterbox("你的姓名")
floor = easygui.enterbox("你所在的街道门排")
city = easygui.enterbox("你所在的省、市")
stamp = easygui.enterbox("邮编")

easygui.msgbox("--------------\n"+
        name+"\n"+
        floor+"\n"+
        city+"\n"+
        stamp+"\n"+
        "--------------")
