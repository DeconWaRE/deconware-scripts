# @ImageJ ij
# @DisplayService display

from net.imglib2.meta import ImgPlus

# create a new blank image
from jarray import array
dims = array([150, 100], 'l')
blank = ij.op().createImg(dims)

#display.createDisplay("blank", ImgPlus(blank));
ij.ui().show(blank);

'''
# fill in the image with a sinusoid using a formula
formula = "10 * (Math.cos(0.3*p[0]) + Math.sin(0.3*p[1]))"
sinusoid = ij.op().equation(blank, formula)

# add a constant value to an image
ij.op().add(sinusoid, 13.0)

# generate a gradient image using a formula
gradient = ij.op().equation(ij.op().createImg(dims), "p[0]+p[1]")

# add the two images
composite = ij.op().createImg(dims)
ij.op().add(composite, sinusoid, gradient)

# display the images
ij.ui().show("sinusoid", ImgPlus(sinusoid))
ij.ui().show("gradient", gradient)
ij.ui().show("composite", composite)'''