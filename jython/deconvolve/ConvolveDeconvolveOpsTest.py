# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

from net.imglib2.meta import ImgPlus
from net.imglib2.type.numeric.real import FloatType


from jarray import array

# define a local directory to get the images from
directory="/home/bnorthan/Brian2014/Projects/deconware2/deconware-scripts/images/"

imageName="Bars72.tif"
psfName="BornWolf72.tif"

# open the image
image=data.open(directory+imageName)
display.createDisplay(image.getName(), image);	

thesum=ops.sum(FloatType(), image)
print thesum

# open the psf
psf=data.open(directory+psfName)
display.createDisplay(psf.getName(), psf);

psfsum=ops.sum(FloatType(), psf)
print psfsum

convolved=ops.convolve(image, psf);
display.createDisplay("convolved", ImgPlus(convolved));

outsum=ops.sum(FloatType(), convolved)
print outsum

size=array([0, 0, 0], 'l')
convolved2=ops.convolve(None, image, psf, size)
display.createDisplay("convolved2", ImgPlus(convolved2));

outsum2=ops.sum(FloatType(), convolved2)
print outsum2
print thesum.getRealDouble()
print psfsum.getRealDouble()
print thesum.getRealDouble()*psfsum.getRealDouble()

deconvolved=ops.run("deconvolve", convolved, psf, 10);
display.createDisplay("deconvolved", ImgPlus(deconvolved));
'''

# normalize the psf
ops.run("normalizesum", psf.getImgPlus())

# convolve
convolved=ops.run("Convolution", image.getImgPlus(), psf.getImgPlus())
display.createDisplay("convolved",  data.create(convolved));
"""