# @ImageJ ij

# create a new blank image
from jarray import array
dims = array([150, 100], 'l')
blank = ij.op().createimg(dims)

# fill in the image with a sinusoid using a formula
formula = "10 * (Math.cos(0.3*p[0]) + Math.sin(0.3*p[1]))"
sinusoid = ij.op().equation(blank, formula)

# add a constant value to an image
ij.op().add(sinusoid, 13.0)

# generate a gradient image using a formula
gradient = ij.op().equation(ij.op().createimg(dims), "p[0]+p[1]")

# add the two images
composite = ij.op().createimg(dims)
ij.op().add(composite, sinusoid, gradient)

# display the images
ij.ui().show("sinusoid", sinusoid)
ij.ui().show("gradient", gradient)
ij.ui().show("composite", composite)