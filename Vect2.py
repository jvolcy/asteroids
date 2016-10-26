'''
2D vector class
'''
import math

class Vect2(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '[' + format(self.x, '0.4f') + 'i + ' + format(self.y, '0.4f') + 'j]'

    def __add__(self, rhs_vector):
        return Vect2(self.x + rhs_vector.x, self.y + rhs_vector.y)

    def __sub__(self, rhs_vector):
        return Vect2(self.x - rhs_vector.x, self.y - rhs_vector.y)

    def __mul__(self, rhs_scalar):
        return Vect2(self.x * rhs_scalar, self.y * rhs_scalar)

    def __div__(self, rhs_scalar):
        return Vect2(self.x / rhs_scalar, self.y / rhs_scalar)

    def magnitude(self):
        return(math.sqrt(self.x **2 + self.y**2))

    def angle(self):
        return math.atan2(-self.y, self.x)

    def unit_vector(self):
        mag = self.magnitude()
        if mag == 0:
            return Vect2(1, 0)
        else:
            return Vect2(self.x/mag, self.y/mag)

    
if __name__ == "__main__":
    point1 = Vect2(3, 4)
    point2 = Vect2(1, 1)
    point3 = point1 * 2
    print (point3)


        
