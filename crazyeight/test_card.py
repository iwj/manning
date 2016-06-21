# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-05-31
# Author: juzi
# E-mail: jentlewoo@gmail.com

import random
from cards import Card

# 定义一个牌组
deck = []
# 遍历全部花色全部点数，并依次添加到 deck 中
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        deck.append(Card(suit_id, rank_id))
        print "正在生成"+deck[-1].short_name


# 定义一个手牌
hand = []
for cards in range(0, 5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print "缩写\t全称\t分数"
for card in hand:
    print card.short_name, "=" , card.long_name, " Value:" , card.value
