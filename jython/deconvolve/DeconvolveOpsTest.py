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

# RLTV default extension non-circulant true
#deconvolved=ops.run("deconvolve.richardsonLucyTV", None, image, psf, [0,0,0], None, None, None, None, None, None, 20, 0.005, True, True);
deconvolved=ops.deconvolve().richardsonLucyTV(None, image, psf, [0,0,0], None, None, None, None, None, None, 20, 0.005, True, True);

#deconvolved=ops.deconvolve().richardsonLucy(None, image, psf, [0,0,0], None, None, None, None, None, None, 2, True, True);

# RL default extension non-circulate true
#deconvolved=ops.run("deconvolve.richardsonLucy", None, image, psf, None, None, None, None, None, None, None, 2, True, False);

#deconvolved=ops.run("deconvolve.richardsonlucy", None, image, psf, None, None, None, None, None, None, None, 2, True, False);

# default extension, non-circulant false
#deconvolved=ops.run("rltv", None, image, psf, None, 20, 0.005);

# no extension
#deconvolved=ops.run("rltv", None, image, psf, [0,0,0], 2, 0.005);

# deconvolve with rl
#deconvolved=ops.run("deconvolve.richardsonlucy", None, image, psf, [0,0,0], 20);
# turn non-circulant off
#deconvolved=ops.run("deconvolve.richardsonlucy", None, image, psf, [0,0,0],  None, None, None, None, None, None, 20, False);
#deconvolved=ops.run("deconvolve.richardsonlucy", None, image, psf, None, 20);
# show the deconvolved result
display.createDisplay("deconvolved", ImgPlus(deconvolved));
