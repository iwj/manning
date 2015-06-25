# -*- coding:utf-8-*-
"""
华氏度转摄氏度gui
"""

import easygui


f_degree = easygui.enterbox("请输入华氏度")
c_degree = (float(f_degree) - 32) * 5.0 / 9
easygui.msgbox("result = " + str(c_degree) +"摄氏度")
