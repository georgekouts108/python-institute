import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        #
        # Write code here
        #
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        #
        # Write code here
        #
        return self.__x

    def gety(self):
        #
        # Write code here
        #
        return self.__y

    def distance_from_xy(self, x, y):
        #
        # Write code here
        #
        X, Y = (float(x), float(y))
        x, y = (self.__x, self.__y)
        csq = (abs(X - x))**2 + (abs(Y - y))**2
        
        return csq ** 0.5
        

    def distance_from_point(self, point):
        #
        # Write code here
        #
        X, Y = (float(point.getx()), float(point.gety()))
        x, y = (self.__x, self.__y)
        csq = (abs(X - x))**2 + (abs(Y - y))**2
        
        return csq ** 0.5


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
