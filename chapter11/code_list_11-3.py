numBlocks = int(raw_input ("How many blocks do you want?"))
numLines = int(raw_input ("How many lines per block do you want?"))
numStars = int(raw_input ("How many stars per line do you want?"))
for block in range(0, numBlocks):
    for line in range(0, numLines):
        for star in range(0, numStars):
            print "* ",
        print
    print
