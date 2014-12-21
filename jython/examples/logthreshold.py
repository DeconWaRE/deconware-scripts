# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @UIService ui
# @net.imagej.Dataset inputData

from net.imglib2.img.planar import PlanarImgFactory;
from net.imglib2.type.numeric.real import FloatType;
from net.imglib2.meta import ImgPlus
from net.imglib2.img.display.imagej import ImageJFunctions

from jarray import array
from ij import IJ

# create a log kernel
logKernel=ops.logKernel(2, 1.0);

# create an image for the result
logFiltered=ops.createImg(PlanarImgFactory(), FloatType(), \ 
	array([inputData.dimension(0), inputData.dimension(1)], 'l'))

# convolve and display
ops.convolve(logFiltered, inputData, logKernel);
display.createDisplay("log", ImgPlus(logFiltered));

# otsu threshold and display
thresholded = ops.run("otsu", logFiltered)
display.createDisplay("thresholded", ImgPlus(thresholded));

# convert to imagej1 image plus so we can run analyze particles
impThresholded=ImageJFunctions.wrap(thresholded, "wrapped")

# convert to mask and analyze particles
IJ.run(impThresholded, "Convert to Mask", "")
IJ.run(impThresholded, "Analyze Particles...", "display add");
IJ.run("Close"); 
