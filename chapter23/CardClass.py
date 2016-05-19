# -*- coding:utf-8 -*-

class Card:
    def __init__(self, color_id, rank_id):
        self.rank_id = rank_id
        self.color_id = color_id

        if self.rank_id == 1:
            self.rank = "Ace"
            self.value = 1
        elif self.rank_id == 11:
            self.rank = "Jack"
            self.value = 10
        elif self.rank_id == 12:
            self.rank = "Queen"
            self.value = 10
        elif self.rank_id ==13:
            self.rank = "King"
            self.value = 10
        elif 2 <= self.rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        else:
            self.rank = "RankError"
            self.value = -1

        if self.color_id == 1:
            # self.suit = "Diamonds"
            self.suit = "方片"
        elif self.color_id == 2:
            # self.suit = "Hearts"
            self.suit = "红桃"
        elif self.color_id == 3:
            # self.suit = "Spades"
            self.suit = "梅花"
        elif self.color_id == 4:
            # self.suit = "Clubs"
            self.suit = "黑桃"
        else:
            self.suit = "SuitError"
        self.short_name = self.rank[0]+self.suit
        if self.rank == "10":
            self.short_name = self.rank + self.suit
        self.long_name = self.rank + " of " + self.suit
