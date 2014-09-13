from jarray import zeros
from random import randrange

class Add3DShapes(object):
	def __init__(self, ops):
		self.ops=ops
	
	def add3To1Sphere(self, hyperSlice, location, intensity):

		aradius=zeros(3,'l')
		aradius[0]=10
		aradius[1]=10
		aradius[2]=30
		
		self.ops.run("addassymetricsphere",  hyperSlice, location, intensity, aradius)

	def addZEdgeSphere(self, hyperSlice, intensity, radius):
		location=[hyperSlice.dimension(1)/2, hyperSlice.dimension(2)/2, radius]
		self.ops.run("addsphere", hyperSlice, location, intensity, radius) 

	def addCenterSphere(self, hyperSlice, intensity, radius):
		location=[hyperSlice.dimension(0)/2, hyperSlice.dimension(1)/2, hyperSlice.dimension(2)/2]
		print location
		self.ops.run("addsphere", hyperSlice, location, intensity, radius)

	def addRandomPointsInROI(self, hyperSlice, intensity, num):
		
		aradius=zeros(3,'l')
		aradius[0]=1
		aradius[1]=1
		aradius[2]=3
		
		xSize=hyperSlice.dimension(0)
		ySize=hyperSlice.dimension(1)
		zSize=hyperSlice.dimension(2)

		for n in range(0, num-1):
			randomPoint=[ randrange(0, xSize-1), randrange(0, ySize-1), randrange(zSize/2-5, zSize/2+5)]			
			self.ops.run("addassymetricsphere",  hyperSlice, randomPoint, intensity, aradius)
			