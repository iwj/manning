print "Which multiplication table would you like?"

like = int(raw_input())

print "Here is your table:"

for i in range(1, 11):
    print i , "x" , like , "=" , i*like
