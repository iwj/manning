numLines = int(raw_input ("How many lines do you want?"))
numStars = int(raw_input ("How many stars per line do you want?"))
for line in range(0, numLines):
    for star in range(0, numStars):
        print "* ",
    print
