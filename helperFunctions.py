import math
# from point import Point

class Point:
    def __init__(self, X, Y, Id):
        self.X = X
        self.Y = Y
        self.Id = Id

def scale(points):
    minX, maxX, minY, maxY = math.inf, -math.inf, math.inf, -math.inf
    for point in points:
        minX = min(minX, point.X)
        minY = min(minY, point.Y)
        maxX = max(maxX, point.X)
        maxY = max(maxY, point.Y)
    size = max(maxX - minX, maxY - minY)
    scaledPoints = []
    for point in points:
        qx = (point.X - minX)/size
        qy = (point.Y - minY)/size
        scaledPoints.append(Point(qx, qy, point.Id))
    return scaledPoints

def pathLength(points):
	d = 0.0
	for i in range(1, len(points)):
		if points[i].Id == points[i-1].Id :
			d += distance(points[i-1], points[i])
	return d

def distance(p1, p2):
    dx = p2.X - p1.X
    dy = p2.Y - p1.Y
    return math.sqrt((dx * dx) + (dy * dy))

def centroid(points):
    x, y = 0.0, 0.0
    numPoints = len(points)
    for point in points:
        x += point.X
        y += point.Y
    x /= numPoints
    y /= numPoints
    return Point(x, y, 0)

def TranslateTo(points, pt):
	c = centroid(points)
	newpoints = []
	for i in range(len(points)):
		qx = points[i].X + pt.X - c.X
		qy = points[i].Y + pt.Y - c.Y
		newpoints.append(Point(qx, qy, points[i].Id))
	return newpoints

def Resample(points, n):
    I = pathLength(points) / (n - 1)
    print("pl", pathLength(points), I)
    D = 0.0
    newpoints = []
    newpoints.append(points[0])
    #len(points)
    # for i in range(len(points)):
    i = 1
    while(i<len(points)):
        if (points[i].Id == points[i-1].Id):
            d = distance(points[i-1], points[i])
            if ((D + d) >= I) :
                qx = points[i-1].X + ((I - D) / d) * (points[i].X - points[i-1].X)
                qy = points[i-1].Y + ((I - D) / d) * (points[i].Y - points[i-1].Y)
                q = Point(qx, qy, points[i].Id)
                newpoints.append(q)
                points.insert(i, q)
                D = 0.0
            else:
                D += d
        i+=1
    if (len(newpoints) == n - 1):
        newpoints.append(Point(points[len(points) - 1].X, points[len(points) - 1].Y, points[len(points) - 1].Id))
    return newpoints

def CloudDistance(pts1, pts2, start):
    lenPts1 = len(pts1)
    matched = []
    for _ in range(lenPts1):
        matched.append(False)
    currSum = 0
    i = start
    while True:
        index = -1
        min = math.inf
        for j in range(len(matched)):
            if not matched[j]:
                #print(i, " j:",j, lenPts1, len(pts2), len(matched))
                d = distance(pts1[i], pts2[j])
                if d < min:
                    min = d
                    index = j
        matched[index] = True
        weight = 1 - ((i - start + lenPts1) % lenPts1) / lenPts1
        currSum += weight * min
        i = (i + 1) % lenPts1
        if i == start:
            break
    return currSum

def GreedyCloudMatch(points, P):
    e = 0.50
    step = math.floor(math.pow(len(points), 1.0 - e))
    minVal = math.inf
    for i in range(0, len(points), step):
        d1 = CloudDistance(points, P.points, i)
        #print(len(P.points), len(points))
        d2 = CloudDistance(P.points, points, i)
        minVal = min(minVal, min(d1, d2))
    return minVal

