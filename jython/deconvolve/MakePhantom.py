# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

# empty image

from jarray import zeros
from net.imglib2.type.numeric.real import FloatType
from net.imglib2.meta import ImgPlus

size=zeros(3,'i')
size[0]=128
size[1]=128
size[2]=64

image=ops.run("create", size,  FloatType())

imgPlus=ImgPlus(image, "phantom")

display.createDisplay("phantom",  data.create(imgPlus));

location=zeros(3,'i')
location[0]=size[0]/2;
location[1]=size[1]/2;
location[2]=size[2]/2;

radius1=20
radius2=17

aradius=zeros(3,'l')
aradius[0]=10
aradius[1]=10
aradius[2]=30

#ops.run("addsphere",  image, location, radius, 1.0)
#ops.run("addassymetricspherel",  image, location, 1.0, radius1, radius2)
ops.run("addassymetricsphere",  image, location, 1.0, aradius)



