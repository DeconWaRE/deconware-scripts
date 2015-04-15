# @DisplayService display
# @OpService ops
# @Integer numDimensions
# @Float sigma

from net.imglib2.meta import ImgPlus

gaussianKernel =ops.gaussKernel( numDimensions, sigma);
display.createDisplay("gausskernel", ImgPlus(gaussianKernel));