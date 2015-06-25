# -*- coding:utf-8 -*-

for just_print_star in range(0, 10):
    print "* ",
print "\n要想阅读《深入理解计算机系统》，请先登录"
password = "it_is_not_the_true_key"
while not password == "h!":
    for just_print_star in range(0, 10):
        print "* ",
    print "\n用户名：admin"
    password = raw_input("密..码：")
else:
    for just_print_star in range(0, 10):
        print "* ",
    print "\n好，我借给你，我的联系方式\nPhone:155 5816 9723\nE-mail:jentlewoo@gmail.com"
