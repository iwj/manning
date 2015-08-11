import time


start_time = int(raw_input("How many seconds? "))
for i in range(start_time, 0, -1):
    print i,
    for j in range(i, 0, -1):
        print "*",
    print
    time.sleep(1)
print "BLAST OFF!"
