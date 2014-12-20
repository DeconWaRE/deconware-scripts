# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

import sys

from com.deconware.algorithms.dim.ExtendImageUtility import BoundaryType
from com.deconware.algorithms.fft.SimpleFFTFactory import FFTTarget
from com.deconware.ops.fft import ConvolutionRaiRai

jythondir="/home/bnorthan/Brian2012/Round2/deconware2/deconware-scripts/jython/"

phantomdir=jythondir+"phantom/"
psfdir=jythondir+"psf/"

sys.path.append(phantomdir)
sys.path.append(psfdir)

import MultiChannelPhantom
reload(MultiChannelPhantom)
#import CreatePsf
#reload(CreatePsf)

from MultiChannelPhantom import MakeMultiChannelPhantom
#from CreatePsf import CreatePsf

size=[128, 128, 64, 3]

# create the phantom
phantom=MakeMultiChannelPhantom(ops, size)
#MakeMultiChannelPhantom([256, 256, 128, 5])
display.createDisplay("phantom",  data.create(phantom));

# create the psf
# psfOp=Psf([.1, .1, .3], [400, 500, 600], 1.4, 1.51, 1.51, 10)
psf = ops.run("psf", size[0], size[2], [100, 100, 300], [400, 500, 600], 1.4, 1.51, 1.51, 10)
display.createDisplay("psf",  data.create(psf));

extended = ops.run("extend", None, phantom, 10, 20, BoundaryType.ZERO, FFTTarget.MINES_SPEED)
display.createDisplay("extended",  data.create(extended));

extendedPsf = ops.run("extend", None, psf, 10, 20, BoundaryType.ZERO, FFTTarget.MINES_SPEED)
display.createDisplay("extended psf",  data.create(extendedPsf));

# convolve
convolved=ops.run("frequencyfilter", extended, extendedPsf, ConvolutionRaiRai())
display.createDisplay("convolved",  data.create(convolved));


