class Triangle():
    def __init__(self):
        self.sides = 3
        self.angle = 180

    def checkSides(self, sides):
        if sides == self.sides:
            return True
        return False

    def checkAngle(self, angle):
        if angle == self.angle:
            return True
        return False


abc = Triangle()

print("This is Triangle: ", abc.checkSides(4))
print("Sum of the angles is 180: ", abc.checkAngle(360))