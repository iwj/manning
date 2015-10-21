class Ball:

    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()
myBall.direction = "down"
myBall.color = "red"
myBall.size = "big"

print "* "*8
print "I just create a ball."
print "My ball is", myBall.size
print "My ball is", myBall.color
print "My ball's direction is", myBall.direction
print "* "*8
print "Now I'm going to bounce the ball"
print 
myBall.bounce()
print "Now, the ball's direction is", myBall.direction

print myBall
