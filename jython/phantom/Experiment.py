from net.imglib2.type.numeric.real import FloatType
from net.imglib2.meta import ImgPlus
from net.imglib2.meta import Axes
from net.imglib2.meta import AxisType

class Experiment(object):
	def __init__(self, measurementSizeX, measurementSizeY, measurementSizeZ, psfSizeX, psfSizeY, psfSizeZ, numChannels, homeDirectory, ops):
		self.homeDirectory=homeDirectory
		self.ops=ops
		
		# size of the measurement 
		self.measurementSizeX=measurementSizeX
		self.measurementSizeY=measurementSizeY
		self.measurementSizeZ=measurementSizeZ

		# size of the psf
		self.psfSizeX=psfSizeX
		self.psfSizeY=psfSizeY
		self.psfSizeZ=psfSizeZ
		self.numChannels=numChannels

		# size of the object space
		self.objectSizeX=measurementSizeX+psfSizeX-1
		self.objectSizeY=measurementSizeY+psfSizeY-1
		self.objectSizeZ=measurementSizeZ+psfSizeZ-1

	def CreatePhantom(self):
		if (self.numChannels>1):
			image=self.ops.run("create", [self.objectSizeX, self.objectSizeY, self.objectSizeZ, self.numChannels],  FloatType())
		else:
			image=self.ops.run("create", [self.objectSizeX, self.objectSizeY, self.objectSizeZ],  FloatType())

		ax=[Axes.X, Axes.Y, Axes.Z, Axes.CHANNEL]
		self.phantom=ImgPlus(image, "phantom", ax)