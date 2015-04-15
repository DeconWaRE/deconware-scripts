# @DisplayService display
# @OpService ops
# @net.imagej.Dataset image
# @net.imagej.Dataset psf

from net.imglib2.meta import ImgPlus
from jarray import array


# by default when we deconvolve the image is extended to avoid wrap around during convolution
#deconvolved=ops.run("deconvolve", image, psf, 10);

# alternatively we can define an extension size.  Here we set the extension size to be 0 in all dimensions
# this means the image won't be extended (other then extension that is done internally to reach a fast fft size)
size=array([0, 0, 0], 'l')
#deconvolved=ops.run("rltv", None, image, psf, size, 10, 0.001);
deconvolved=ops.run("deconvolve.richardsonlucy", None, image, psf, size, 50);
display.createDisplay("deconvolved", ImgPlus(deconvolved));
