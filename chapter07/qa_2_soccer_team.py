sex = raw_input("What is your sex?(m = male, f = famale)")

if sex == "m":
    print "Bye bye."
elif sex == "f":
    age = int (raw_input("And age"))
    if 10 <= age <= 12:
        print " P A S S"
    else:
        print "Bye bye"
