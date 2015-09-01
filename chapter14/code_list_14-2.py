class Ball:
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"

myBall = Ball()
myBall.direction = "down"
myBall.color = "red"

print "* "*8
print "My ball is", myBall.direction
print "My ball is", myBall.color
print "Now let's bounce"
print
myBall.bounce()
print"Now the ball's direction is", myBall.direction
