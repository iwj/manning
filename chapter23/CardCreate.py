# -*- coding:utf-8 -*-

import random
from CardClass import Card


deck = []
for color_id in range(1, 5):
    for rank_id in range(1, 14):
        deck.append(Card(color_id, rank_id))
hand = []
for cards in range(0, 5):
    a = random.choice(deck)
    hand.append(a)#牌放到新数组hand里，表示拿出来
    deck.remove(a)#移除已经拿走的牌

print
for card in hand:
    print card.short_name, " => ", card.long_name, "Value:", card.value
