# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

# empty image

from jarray import zeros
from jarray import array
from net.imglib2.type.numeric.real import FloatType
from net.imglib2.meta import ImgPlus

size=array([144, 144], 'i')
image=ops.createimg(size)

location=array([size[0]/2, size[1]/2], 'i')

radius1=20
radius2=17

aradius=array([20, 20], 'i')

#ops.run("addsphere",  image, location, radius, 1.0)
#ops.run("addassymetricspherel",  image, location, 1.0, radius1, radius2)
ops.run("addassymetricsphere",  image, location, 1.0, aradius)

display.createDisplay("phantom",  image);




