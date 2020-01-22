import math
from pointCloud import PointCloud
from helperFunctions import Point, GreedyCloudMatch
import pickle

class Recognizer:
    def __init__(self):
        self.pointClouds = []

    def setPointCloudsDemo(self):
        self.pointClouds.append(PointCloud("T", [Point(30,7,1), Point(103,7,1),
		Point(66,7,2),Point(66,87,2)]))
        self.pointClouds.append(PointCloud("N", [Point(177,92,1),Point(177,2,1),Point(182,1,2),Point(246,95,2),
		Point(247,87,3),Point(247,1,3)]))


    
    def recognize(self, points):
        candidate = PointCloud("", points)
        #print("here", len(points))
        u = -1
        b = math.inf
        for i in range(len(self.pointClouds)):
            d = GreedyCloudMatch(candidate.points, self.pointClouds[i])
            if (d < b):
                b = d
                u = i
        return "No match" if u == -1 else self.pointClouds[u].name

    def addGesture(self, name, points):
        self.pointClouds.append(PointCloud(name, points))
        num = 0
        for i in range(len(self.pointClouds)):
            if self.pointClouds[i].name == name:
                num+=1
        return num


    