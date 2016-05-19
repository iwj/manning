# -*- coding:utf-8 -*-


file_path = "./note.md"
#file_path = "../README.md"
file_note = open(file_path, "r")
lines = file_note.readlines()
#print lines
print type(lines)
for i in range(5):
    a = file_note.readline()
    print a
    print type(a)
#for line_one in lines:
    #print line_one
file_note.close()

print "* "*8
print "二进制打开文件："
file_binary = open(file_path, "rb")
print type(file_binary)
for i in file_binary:
    print i
    print type(i)
file_binary.close()

print "* "*8
print "a 参数 追加："
file_add = open(file_path, "a")
file_add.write("\n我无法吞下玻璃。")
file_add.close()
