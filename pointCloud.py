from helperFunctions import scale, Point, pathLength, Resample, TranslateTo
import math


class PointCloud:
    def __init__(self, name, points):
        self.name = name
        self.numPoints = 32
        self.Origin = Point(0,0,0)
        self.points = scale(points)
        print("pc",len(self.points))
        self.points = Resample(self.points, self.numPoints)
        print("pc",len(self.points))
        self.points = TranslateTo(self.points, self.Origin)
        print("pc",len(self.points))


