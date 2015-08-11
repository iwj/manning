# -*- coding:utf-8 -*-

name = []
for i in range(0,5):
    name.append(raw_input("Input name: "))
print "The names are",
for i in range(0, 5):
    print name[i],

print "Sorted list:"
print "[1]"
name_sorted = name[:]#将原始列表复制给name_sorted
name_sorted.sort()#name_sort 开始排序，完成后仍然是同一个变量名
for i in range(0,5):
    print name_sorted[i],
print "\n[2]"

name_sorted_2 = sorted(name)
for i in range(0, 5):
    print name_sorted_2[i],
