# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

from net.imglib2.meta import ImgPlus

# define a local directory to get the images from
directory="/home/bnorthan/Brian2012/Round2/deconware2/deconware-scripts/images/"

imageName="Bars.tif"
psfName="BornWolf.tif"

# open the image
image=data.open(directory+imageName)
display.createDisplay(image.getName(), image);	

# open the psf
psf=data.open(directory+psfName)
display.createDisplay(psf.getName(), psf);

convolved=ops.convolve(image, psf);
display.createDisplay("convolved", ImgPlus(convolved));

deconvolved=ops.run("deconvolve", convolved, psf, 10);
display.createDisplay("deconvolved", ImgPlus(deconvolved));


"""
# normalize the psf
ops.run("normalizesum", psf.getImgPlus())

# convolve
convolved=ops.run("Convolution", image.getImgPlus(), psf.getImgPlus())
display.createDisplay("convolved",  data.create(convolved));
"""