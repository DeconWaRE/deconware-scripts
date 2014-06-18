# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops
# @UIService ui

from net.imglib2.meta import Axes
from jarray import zeros

# size in pixels
size=zeros(3,'i')
size[0]=100
size[1]=100
size[2]=50

# spacing in microns
spacing=zeros(3,'f')
spacing[0]=100
spacing[1]=100
spacing[2]=300

# emission wavelenth
EMW= 500

# numerical aperture
NA=1.4

# actual oil refractive index
RI_lens_actual=1.51

# actual specimen layer refractive index
RI_specimen_actual=1.51

# depth below coverslip in microns
depth=10

psf=ops.run("psf", size, spacing, EMW, NA, RI_lens_actual, RI_specimen_actual, depth)
display.createDisplay("convolved",  data.create(psf));


