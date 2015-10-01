# @OpService ops
# @Dataset data
# @UIService ui
# @DisplayService display

# to run this tutorial run 'file->Open Samples->Confocal Series' and make sure that
# confocal-series.tif is the active image

from net.imglib2.util import Intervals
from net.imagej.axis import Axes

# first take a look at the size and type of each dimension
for d in range(data.numDimensions()):
	print "axis d: type: "+str(data.axis(d).type())+" length: "+str(data.dimension(d))

img=data.getImgPlus()

cropDims=[]

for d in range(data.numDimensions()):
	print "axis d: type: "+str(data.axis(d).type())+" length: "+str(data.dimension(d))

for d in range(data.numDimensions()): cropDims.append(data.dimension(d)/4)
for d in range(data.numDimensions()): cropDims.append(3*(data.dimension(d)/4)-1)

cropped=ops.image().crop(img, Intervals.createMinMax(cropDims))
ui.show(cropped)
