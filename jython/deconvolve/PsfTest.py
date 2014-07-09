# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @UIService ui

from net.imglib2.meta import Axes
from jarray import zeros

# size in pixels
xySize=100
zSize=50

# spacing in nanos
spacing=zeros(3,'f')
spacing[0]=100
spacing[1]=100
spacing[2]=300

# emission wavelenth in nanos
# note: if the emission wavelength is an array it will generate an psf for each channel
emw= zeros(3,'f')
emw[0]=400
emw[1]=500
emw[2]=600

# numerical aperture
NA=1.4

# actual oil refractive index
RI_lens_actual=1.51

# actual specimen layer refractive index
RI_specimen_actual=1.51

# depth below coverslip in microns
depth=10

psf=ops.run("psf", xySize, zSize, spacing, emw, NA, RI_lens_actual, RI_specimen_actual, depth)
display.createDisplay("convolved",  data.create(psf))




