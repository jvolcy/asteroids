'''
2D vector class
'''
import math

class Vect2(object):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self):
        return '[' + str(self.x) + 'i + ' + str(self.y) + 'j]'
#        return '[' + format(self.x, '0.4f') + 'i + ' + format(self.y, '0.4f') + 'j]'

    @classmethod
    def from_degrees(cls, degrees):
        '''Initialize Vect2 from an angle in degrees'''
        return cls.from_rads(degrees*math.pi/180.0)

    @classmethod
    def from_rads(cls, radians):
        '''Initialize Vect2 from an angle in radians'''
        x = math.cos(radians)
        y = math.sin(radians)
        return Vect2(x, y)

    def __add__(self, rhs_vector):
        return Vect2(self.x + rhs_vector.x, self.y + rhs_vector.y)

    def __sub__(self, rhs_vector):
        return Vect2(self.x - rhs_vector.x, self.y - rhs_vector.y)

    def __mul__(self, rhs_scalar):
        return Vect2(self.x * rhs_scalar, self.y * rhs_scalar)

    def __truediv__(self, rhs_scalar):
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
    #print (point3)

    print("179 -->" , Vect2.from_degrees(179))
    print("-179 -->" , Vect2.from_degrees(-179))
    print("90 -->" , Vect2.from_degrees(90))
    print("-90 -->" , Vect2.from_degrees(-90))


        
