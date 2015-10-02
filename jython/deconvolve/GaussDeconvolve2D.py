# @OpService ops
# @UIService ui
# @Dataset inputData

from net.imglib2.img.display.imagej import ImageJFunctions
from ij import IJ

print inputData.numDimensions()

# create a gauss kernel
kernel=ops.create().kernelGauss(3.0, 3.0)

# deconvolve with guass kernel
filtered=ops.deconvolve().richardsonLucyTV(None, inputData, kernel, None, None, \
 None, None, None, None, None, 10, 0.005, True, True);

# display result
ui.show("deconolved", filtered)


