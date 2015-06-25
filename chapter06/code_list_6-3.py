"""
enterbox
"""


import easygui


flavor = easygui.enterbox("What is your favorite ice cream?")
easygui.msgbox ("you like "+ flavor)
