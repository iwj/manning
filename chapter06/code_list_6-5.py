# -*- coding:utf-8 -*-
"""
Num Guess in GUI
"""

import easygui
import random


secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("""I will give you 6 tries.
It is a number from 1 to 99.""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("what is yer guess")
    if not guess:
        break
    if guess < secret:
        easygui.msgbox(str(guess) + " is too low.")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high.")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("Avast!i恭喜猜对了")
else:
    easygui.msgbox("No more guesses!没机会了")
