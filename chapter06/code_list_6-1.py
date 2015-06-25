

import easygui

flavor = easygui.buttonbox("Your favorite ice cream flavor?", 
        choices = ["Vanilla", "Chocolate", "Strawberry"])

easygui.msgbox ("Your picked " + flavor)
