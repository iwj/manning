# -*- coding:utf-8 -*-

from CardMark import Card


done = False
p_total = c_total = 0
while not done:
    init_cards()
    while not game_done:
        blocked = 0
        player_turn()#轮到Player
        if len(p_hand) == 0:
            game_done = True
            print
            print "You win!"
        if not game_done:
            computer_turn()#轮到Computer
        if len(c_hand) == 0:
            game_done = True
            print
            print "Computer win."
        if blocked >= 2:
            game_done = True
            print "Both players blocked. G.A.M.E-O.V.E.R."
play_again = raw_input("Play again(Y/N)?")
    if play_again == "Y" or play_again =="y":
        done = False
    else:
        done = True
