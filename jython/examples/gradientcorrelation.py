# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @net.imagej.Dataset image
# @net.imagej.Dataset template

from net.imglib2.img.display.imagej import ImageJFunctions;
from net.imglib2.type.numeric.real import FloatType;
from net.imglib2.type.numeric.complex import ComplexFloatType;

from jarray import array

# create a log kernel
logKernel=ops.logKernel(image.numDimensions(), 1.0);

# or use new convolve that creates the output image
imf=ops.convolve(image, logKernel);
display.createDisplay("log", imf);	

# or use new convolve that creates the output image
tf=ops.convolve(template, logKernel);
display.createDisplay("logt", tf);

correlation=ops.run("correlate", imf, tf)
display.createDisplay("correlation", correlation);
