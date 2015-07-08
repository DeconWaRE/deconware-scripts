# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @net.imagej.Dataset psf

from ij import IJ

from jarray import zeros
from jarray import array
from net.imglib2.type.numeric.real import FloatType
from net.imglib2.meta import ImgPlus
from net.imglib2.img.display.imagej import ImageJFunctions

from com.deconware.algorithms.noise import AddPoissonNoise

size=[256,256,256]
image=ops.createimg(size)

location=[size[0]/2, size[1]/2, size[2]/2+50]
radius1=48
radius2=44

background=0.0
foreground=200.0

#ops.run("addsphere",  image, location, radius, 1.0)
#ops.run("addassymetricspherel",  image, location, 1.0, radius1, radius2)
#ops.run("addassymetricsphere",  image, location, 1.0, aradius)
ops.run("addconstant", image, background)
ops.run("addshell", image, location, foreground, background, radius1, radius2)

# show phantom
display.createDisplay("phantom",  image);

# crop phantom (replace with crop op)
impPhantom=IJ.getImage()
impPhantom.setRoi(56, 56,144,144);
IJ.run(impPhantom, "Crop", "");
IJ.run(impPhantom, "Make Substack...", "frames=56-199");

# convolve
convolved=ops.convolve(image, psf);

# add poisson noise
noiser=AddPoissonNoise(convolved)
noiser.process()

# show convolved
display.createDisplay("convolved",  ImgPlus(convolved));

# crop convolved (replace with crop op)
impConvolved=IJ.getImage()
impConvolved.setRoi(56, 56,144,144);
IJ.run(impConvolved, "Crop", "");
IJ.run(impConvolved, "Make Substack...", "frames=56-199");
