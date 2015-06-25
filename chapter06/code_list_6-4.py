"""
default value
"""

import easygui


flavor = easygui.enterbox("What",
        default = "Volvo")
easygui.msgbox ("You "+ flavor)
