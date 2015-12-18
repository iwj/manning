#! /usr/bin/env
# -*- coding:utf-8-*-

class Ball:
    def __init__ (self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def __str__(self):
        msg_test = "嘿，我正在测试。"
        msg = "Hi, I'm a " + self.size + " " + self.color + " ball!"
        return msg_test

myBall = Ball("red", "big", "down")
print myBall

