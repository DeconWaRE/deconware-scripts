# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

from net.imglib2.img.display.imagej import ImageJFunctions;
from net.imglib2.type.numeric.real import FloatType;
from net.imglib2.type.numeric.complex import ComplexFloatType;

from jarray import array

# define a local directory to get the images from
directory="/home/bnorthan//Brian2012/Round2/deconware2/imglib2-tutorials/"

imageName="DrosophilaWing.tif"
templateName="WingTemplate.tif"

# open and display the image
image=data.open(directory+imageName)
display.createDisplay(image.getName(), image);	

# open and display the template
template=data.open(directory+templateName)
display.createDisplay(template.getName(), template);	

# fft of the template
templateFFT=ops.fft(template.getImgPlus());
ImageJFunctions.show(templateFFT).setTitle("fft power spectrum");

# complex invert the kernel
c = ComplexFloatType();
for  t in templateFFT:
	c.set(t);
	t.complexConjugate();
	c.mul(t);
	t.div(c);

# create Img memory for inverse FFT and compute inverse 
templateInverse=ops.createimg(array([template.dimension(0), template.dimension(1)], 'l'))
ops.ifft(templateInverse, templateFFT)
display.createDisplay("template inverse", templateInverse)

# convolve templateInverse with image
final=ops.convolve(image, templateInverse);
display.createDisplay("final", final)
	