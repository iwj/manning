print "Which multiplication table would you like?"

like = int(raw_input())

print "Here is your table:"
i = 1

while i < 11:
    print i , "x" , like , "=" , i*like
    i+=1
