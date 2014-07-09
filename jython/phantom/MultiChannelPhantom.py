# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

# empty image

from jarray import zeros
from net.imglib2.type.numeric.real import FloatType
from net.imglib2.meta import ImgPlus
from net.imglib2.meta import Axes
from net.imglib2.meta import AxisType
from net.imagej.ops.slicer import CroppedIterableInterval
from net.imglib2.view import Views
import sys
sys.path.insert(0, '/home/bnorthan/Brian2014/Projects/deconware2/deconware-scripts/jython/phantom/')

import Phantom
reload(Phantom)
from Phantom import Add3DShapes

def MakeMultiChannelPhantom (ops, size):

	if len(size)>3:
		numChannels=size[3]
	else:
		numChannels=1

	image=ops.run("create", size,  FloatType())
	ax=[Axes.X, Axes.Y, Axes.Z, Axes.CHANNEL]
	imgPlus=ImgPlus(image, "phantom", ax)
	
	location=zeros(3,'i')
	location[0]=40;
	location[1]=size[1]/2;
	location[2]=size[2]/2;
	
	#ops.run("addsphere",  image, location, radius, 1.0)
	#ops.run("addassymetricspherel",  image, location, 1.0, radius1, radius2)

 	shapes=Add3DShapes(ops, size)
	
	for d in range(0,numChannels):
		hyperSlice= Views.hyperSlice(image, 3, d)
		#shapes.add3To1Sphere(hyperSlice, location, 1.0)
		#shapes.addZEdgeSphere(hyperSlice, 1.0, 10)
		#shapes.addCenterSphere(hyperSlice, 1.0, 10)
		shapes.addRandomPointsInROI(hyperSlice, 1.0, 20)
		location[0]+=10

	return imgPlus

	


