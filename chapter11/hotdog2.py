# -*- coding:utf-8 -*-

print "number\tDog\tBun\tKetchup\tMustard\tOnions\tCalories"
count = 1
for dog in [0, 1]:
    for bun in [0, 1]:
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    print "#", count, "\t",
                    print dog, "\t", bun, "\t", ketchup, "\t",
                    print mustard, "\t", onion, "\t",
                    #计算总当前搭配的总卡路里
                    total_cal = (dog * 140) + (bun * 120) + (ketchup * 80) +\
                            (mustard * 20) + (onion * 40)
                    #输出总卡路里
                    print total_cal
                    count = count + 1
