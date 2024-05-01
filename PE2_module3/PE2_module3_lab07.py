import math


class Point:
    #
    # The code copied from the previous lab.
    #
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


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        #
        # Write code here
        #
        self.__points = [vertice1, vertice2, vertice3]
        
    def perimeter(self):
        #
        # Write code here
        #
        s12 = self.__points[0].distance_from_point(self.__points[1])
        s23 = self.__points[1].distance_from_point(self.__points[2])
        s13 = self.__points[0].distance_from_point(self.__points[2])
        return s12 + s23 + s13


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
