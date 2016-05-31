# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Date  : 2016-05-31
# Author: juzi
# E-mail: jentlewoo@gmail.com

class Card:
    def __init__(self, suit_id, rank_id):
        self.rank_id = rank_id
        self.suit_id = suit_id

        if self.rank_id == 1:
            self.rank = "Ace"
            self.value = 1

        elif self.rank_id == 11:
            self.rank = "Jack"
            self.value = 10

        elif self.rank_id == 12:
            self.rank = "Queen"
            self.value = 10

        elif self.rank_id == 13:
            self.rank = "King"
            self.value = 10

        elif 2 <= self.rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id

        else:
            self.rank = "点数错误"
            self.value = -1
            
        if self.suit_id == 1:
            self.suit = "方块"
        elif self.suit_id == 2:
            self.suit = "红桃"
        elif self.suit_id == 3:
            self.suit = "黑桃"
        elif self.suit_id == 4:
            self.suit = "梅花"
        else:
            self.suit = "花色错误"

        self.short_name = self.rank[0] + self.suit[0:6]
        if self.rank == '10':
            self.short_name = self.rank + self.suit[0:6]
        self.long_name = self.rank + " of " + self.suit
