# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-05-29
# Author: juzi
# E-mail: jentlewoo@gmail.com


import random
from cards import Card

"""
init 新建一副牌
一副牌
玩家5张
电脑5张
"""
def init_cards():
    deck = []
    for suit in range(1, 5):
        for rank in range(1, 14):
            new_card = Card(suit, rank)
            if new_card.rank == 8:
                new_card.value = 50
            deck.append(new_card)

    p_hand = c_hand = []
    for range(0,5):
        card_one = random.choice(deck)
        print "发牌" + card_one.long_name
        p_hand.append(card_one)
        deck.remove(card_one)
        card_two = random.choice(deck)
        print "发牌" + card_two.long_name
        c_hand.append(card_tow)
        deck.remove(card_two)



"""
主循环
"""
done = False
p_total = c_total = 0
while not done:
    game_done = False
    blocked = 0
    init_cards()
    while not game_done:
        player_turn()
        if len(p_hand) == 0:
            game_done = True
            print
            print "You Won"
            p_points = 0
            for card in c_hand:
                p_points += card.value
            p_total += p_points
            print "铁子，你得分%i" % p_points

        if not game_done:
            computer_turn()

        if len(c_hand) == 0:
            game_done = True
            print
            print "Computer Won"
            c_points = 0
            for card in p_hand:
                c_points += card.value
            c_total += c_points
            print "电脑得分%i" % c_points

        if blocked >= 2:
            game_done = True
            print "Both players blocked. GAME OVER 这疙瘩的计分还没写呢"
    play_again = raw_input("铁子，你还玩吗（Y/N）？")
    if play_again.lower() == "y":
        done = false
        print "接着干。但是这疙瘩的计分也没写"
    else:
        done = True
print "公布最后分数：（铁子，记得补上这里的计分）"

"""
显示手牌
"""
print "\n Your hand:"
for card in p_hand:
    print card.short_name,
print " Up card: ", up_card.short_name
if up_card.rank == '8':
    print " Suit is ", active_suit

"""
轮到玩家了
"""
print "铁子，你想干啥？"
response = raw_input ("出一张牌或者敲“draw”摸一张牌：")
valid_play = False
while not valid_play:
    selected_card = None
    while selected+card == None:
        if response.lower() == "draw":
            valid_play = True
            if len(deck) > 0:
                card = random.choice(deck)
                p_hand.append(card)
                deck.remove(card)
                print "铁子，你摸了这张牌", card.short_name
            else:
                print "铁子，没牌了，再瞅瞅别的路子吧"
                blocked += 1

            return
        else:
            for card in p_hand:
                if response.upper() == card.short_name:
                    selected_card = card
            if selected_card == None:
                response = raw_input("干哈，你想作弊还咋地啊，你没有那张牌：")
    if selected_card.rank == '8':
        valid_play = True
        is_eight = True
    elif selected_card.suit == active_suit:
        valid_play = True
    elif selected_card.rank == up_card.rank:
        valid_play = True

    if not valid_play:
        response = raw_input("铁子，别乱来！再出：")

"""
玩家出一张8时，得到新花色
"""
def get_new_suit():
    global active_suit
    got_suit = False
    while not got_suit:
        suit = raw_input("铁子，来选一个花色(黑红梅方)")
        if suit == "黑":
            active_suit = "black"
            got_suit = True
        elif suit == "红":
            active_suit = "red"
            got_suit = True
        elif suit == "梅":
            active_suit = "flower"
            got_suit = True
        elif suit == "方":
            active_suit = "fang"
            got_suit = True
        else:
            print "铁子，你这输入的啥字啊，重输（黑红梅方）"
    print "铁子，你选了", active_suit
