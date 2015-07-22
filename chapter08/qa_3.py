print "Which multiplication table would you like?"

like = int(raw_input())

print "max?"

max = int(raw_input())

print "Here is your table:"
i = 1
range_end = max + 1

while i < range_end:
    print i , "x" , like , "=" , i*like
    i+=1
