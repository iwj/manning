# -*- coding:utf-8 -*-


import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!阿霍！我是死亡之魂，我有一个秘密。"
print "It is a number from 1 to 99. I'll give you 6 tries. 这是一个1到99之间的数，我给你6次机会。"
while guess != secret and tries < 6:
    guess = input("What's yer guess? 请猜数：")
    if guess < secret:
        print "Too low, ye scurvy dog!太低，你这个丧尸。"
    elif guess > secret:
        print "Too high, landlubber!太高，往下着陆啊。"

    tries = tries + 1

if guess == secret:
    print "Avast! Ye got it! Found my secret, ye did!啊瓦斯特，你做到了，找到了我的秘密！"
    print "The secret number was 这个数就是", secret
else:
    print "No more guesses! Better luck next time, matey!没有机会了，祝你下次好运。"
    print "The secret number was 这个数就是", secret
