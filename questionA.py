class Line(object):
	def __init__(self, x1, x2):
		self.x1 = x1
		self.x2 = x2

	def getX1(self):
		return self.x1

	def getX2(self):
		return self.x2
		
"""checks if 2 lines overlap

"""
def overlap(line1, line2):
	x1 = line1.getX1()
	x2 = line1.getX2()
	x3 = line2.getX1()
	x4 = line2.getX2()

	return (x3<x2 & x4>x1)