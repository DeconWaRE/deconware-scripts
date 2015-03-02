# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

from net.imglib2.img.display.imagej import ImageJFunctions;
from net.imglib2.type.numeric.real import FloatType;
from net.imglib2.type.numeric.complex import ComplexFloatType;

from jarray import array

# define a local directory to get the images from
# TODO:  put images in same directory as the script then get the script directory
directory="/home/bnorthan//Brian2012/Round2/deconware2/imglib2-tutorials/"

imageName="DrosophilaWing.tif"
templateName="WingTemplate.tif"

# open and display the image
image=data.open(directory+imageName)
display.createDisplay(image.getName(), image);	

# open and display the template
template=data.open(directory+templateName)
display.createDisplay(template.getName(), template);	

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
