# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @net.imagej.Dataset image
# @net.imagej.Dataset psf

from net.imglib2.meta import ImgPlus
from net.imglib2.type.numeric.real import FloatType

from jarray import array

sumImg=ops.sum(FloatType(), image.getImgPlus())
sumPsf=ops.sum(FloatType(), psf.getImgPlus())

convolved=ops.convolve(image.getImgPlus(), psf.getImgPlus());
display.createDisplay("convolved", ImgPlus(convolved));

size=array([0, 0, 0], 'l')
convolved2=ops.convolve(None, image, psf, size)
display.createDisplay("convolved2", ImgPlus(convolved2));

sumConvolved=ops.sum(FloatType(), convolved)
sumConvolved2=ops.sum(FloatType(), convolved2)

print sumImg.getRealDouble()
print sumPsf.getRealDouble()
print sumImg.getRealDouble()*sumPsf.getRealDouble()
print sumConvolved.getRealDouble()
