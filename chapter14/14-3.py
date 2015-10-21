class Ball:

    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball("red", "big", "down")
print "* " * 8
print "I just created a ball"
print "My ball is", myBall.color
print "My ball is", myBall.size
print "My ball is", myBall.direction
print "* "*8
print "Now I will bounce it"
myBall.bounce()
print "Now my ball is", myBall.direction
