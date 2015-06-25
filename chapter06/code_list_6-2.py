# -*- coding:utf-8 -*-
"""
这次用的是 choicebox
"""


import easygui
user_choice = easygui.choicebox("你最喜欢什么口味的冰淇淋？",
        #choices = ["巧克力a", "香草b", "奶酪c"])
        choices = ["a", "b", "c"])
easygui.msgbox("你喜欢的口味是" + user_choice)
