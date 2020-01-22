from recognizer import Recognizer
from helperFunctions import Point
import os



#recognizer.setPointCloudsDemo()
#print(recognizer.recognize([Point(30,7,1), Point(103,7,1),Point(66,7,2),Point(66,87,2)]))

def readGesturefile(filePath, recognizer):
	f=open(filePath, "r")
	lines = f.readlines()
	gestureName = lines[0]
	currStrokeNo=0
	points =[]
	for i in range(1, len(lines)):
		l = lines[i].rstrip('\n')
		if l == 'END':
			currStrokeNo+=1
		elif l == 'BEGIN':
			continue
		else:
			x, y = l.split(',')
			#print(x,y)
			points.append(Point(float(x), float(y), currStrokeNo))
	recognizer.addGesture(gestureName, points)

def readEventsfile(filePath, recognizer):
	f=open(filePath, "r")
	lines = f.readlines()
	currStrokeNo=0
	points =[]
	for i in range(len(lines)):
		l = lines[i].rstrip('\n')
		if l == 'MOUSEUP':
			currStrokeNo+=1
		elif l == 'MOUSEDOWN':
			continue
		elif l == 'RECOGNIZE':
			print(recognizer.recognize(points))
			points.clear()
			currStrokeNo = 0
		else:
			x, y = l.split(',')
			points.append(Point(float(x), float(y), currStrokeNo))
	
	
script_dir = os.path.dirname(__file__)
recognizer = Recognizer()
recognizer.setPointCloudsDemo()
readGesturefile(os.path.join(script_dir,'gestureFiles/arrowhead.txt'), recognizer)
readGesturefile(os.path.join(script_dir,'gestureFiles/exclamation_point.txt'), recognizer)
readGesturefile(os.path.join(script_dir,'gestureFiles/five_point_star.txt'), recognizer)
#readGesturefile(os.path.join(script_dir,'gestureFiles/arrowhead.txt'), recognizer)
readEventsfile(os.path.join(script_dir,'eventfiles/arrowhead_eventfile.txt'), recognizer)
print(recognizer.recognize([Point(30,7,1), Point(103,7,1),Point(66,7,2),Point(66,87,2)]))
print(recognizer.recognize([Point(125,343,1),Point(125,341,1),Point(125,338,1),Point(125,335,1),Point(125,331,1),Point(125,319,1),Point(125,311,1),Point(125,303,1),Point(125,295,1),Point(125,286,1),Point(125,278,1),Point(125,268,1),Point(125,265,1),Point(125,257,1),Point(125,251,1),Point(125,245,1),Point(125,240,1),Point(125,230,1),Point(125,227,1),Point(125,222,1),Point(125,218,1),Point(125,214,1),Point(125,210,1),Point(125,205,1),Point(125,201,1),Point(125,196,1),Point(125,191,1),Point(125,186,1),Point(125,182,1),Point(125,180,1),Point(125,176,1),Point(125,173,1),Point(125,170,1),Point(125,168,1),Point(125,166,1),Point(125,163,1),Point(125,162,1),Point(125,160,1),Point(125,159,1),Point(125,157,1),Point(125,157,1),Point(125,156,1),Point(124,156,1),Point(124,156,1),Point(124,155,1),Point(124,155,1),Point(124,155,1),Point(124,156,1),Point(125,157,1),Point(125,157,1),Point(125,158,1),Point(126,159,1),Point(127,160,1),Point(131,162,1),Point(133,164,1),Point(135,166,1),Point(137,169,1),Point(139,171,1),Point(141,174,1),Point(144,177,1),Point(147,181,1),Point(150,186,1),Point(154,190,1),Point(156,195,1),Point(159,200,1),Point(162,204,1),Point(165,209,1),Point(167,213,1),Point(169,217,1),Point(170,220,1),Point(172,223,1),Point(173,227,1),Point(175,230,1),Point(175,231,1),Point(177,234,1),Point(178,236,1),Point(179,239,1),Point(180,241,1),Point(181,245,1),Point(184,250,1),Point(187,255,1),Point(190,260,1),Point(192,263,1),Point(193,264,1),Point(194,266,1),Point(195,267,1),Point(197,269,1),Point(197,269,1),Point(198,270,1),Point(198,270,1),Point(198,271,1),Point(199,271,1),Point(199,271,1),Point(200,272,1),Point(201,272,1),Point(202,273,1),Point(203,274,1),Point(204,276,1),Point(205,277,1),Point(206,278,1),Point(208,279,1),Point(211,282,1),Point(212,283,1),Point(213,284,1),Point(215,285,1),Point(217,287,1),Point(219,289,1),Point(220,290,1),Point(224,293,1),Point(225,294,1),Point(226,296,1),Point(227,296,1),Point(228,297,1),Point(229,298,1),Point(230,299,1),Point(231,300,1),Point(232,301,1),Point(233,302,1),Point(233,303,1),Point(234,304,1),Point(236,306,1),Point(236,307,1),Point(237,308,1),Point(237,308,1),Point(238,309,1),Point(238,309,1),Point(238,310,1),Point(238,310,1),Point(239,310,1),Point(239,310,1),Point(239,311,1),Point(239,311,1),Point(239,311,1),Point(239,311,1),Point(240,312,1),Point(241,314,1),Point(242,317,1),Point(244,320,1),Point(245,321,1),Point(247,324,1),Point(248,326,1),Point(250,328,1),Point(251,329,1),Point(251,330,1),Point(252,331,1),Point(253,331,1),Point(253,332,1),Point(253,332,1),Point(253,332,1),Point(254,333,1),Point(254,333,1),Point(254,333,1),Point(254,333,1),Point(254,333,1),Point(254,333,1),Point(255,333,1),Point(255,333,1),Point(255,333,1),Point(255,334,1),Point(255,334,1),Point(255,334,1),Point(256,335,1),Point(257,337,1),Point(258,339,1),Point(260,341,1),Point(261,343,1),Point(262,345,1),Point(263,347,1),Point(265,349,1),Point(266,350,1),Point(266,351,1),Point(267,352,1),Point(267,352,1),Point(267,353,1),Point(267,353,1),Point(268,353,1),Point(268,353,1),Point(268,353,1),Point(268,352,1),Point(268,352,1),Point(268,351,1),Point(268,351,1),Point(268,349,1),Point(268,346,1),Point(268,345,1),Point(268,344,1),Point(268,341,1),Point(268,335,1),Point(268,333,1),Point(268,331,1),Point(268,328,1),Point(268,311,1),Point(268,309,1),Point(268,307,1),Point(268,300,1),Point(268,287,1),Point(268,282,1),Point(268,277,1),Point(267,264,1),Point(265,259,1),Point(259,237,1),Point(256,227,1),Point(255,223,1),Point(252,214,1),Point(249,207,1),Point(247,199,1),Point(245,191,1),Point(243,183,1),Point(240,176,1),Point(238,170,1),Point(237,167,1),Point(236,163,1),Point(235,160,1),Point(235,158,1),Point(234,156,1),Point(234,156,1),Point(234,155,1),Point(233,154,1),Point(233,154,1),Point(233,154,1),Point(233,154,1),Point(233,153,1),Point(233,153,1),Point(233,153,1),Point(233,153,1),Point(233,153,1),Point(233,152,1),Point(233,152,1),Point(233,151,1),Point(234,149,1),Point(234,148,1),Point(235,147,1),Point(236,146,1),Point(238,143,1),Point(240,140,1),Point(241,139,1),Point(242,137,1),Point(243,136,1),Point(244,135,1),Point(244,134,1),Point(245,134,1),Point(245,134,1),Point(245,133,1),Point(246,133,1),Point(246,133,1),Point(246,133,1),Point(246,134,1),Point(246,134,1),Point(246,134,1),Point(246,135,1),Point(246,135,1)]))