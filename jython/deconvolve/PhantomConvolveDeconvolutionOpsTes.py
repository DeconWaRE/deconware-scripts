# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

import sys
import operator

from com.deconware.algorithms.dim.ExtendImageUtility import ExtensionType
from com.deconware.algorithms.dim.ExtendImageUtility import BoundaryType
from com.deconware.algorithms.fft.SimpleFFTFactory import FFTTarget
from com.deconware.ops.fft import ConvolutionRaiRai

from com.deconware.algorithms.fft.filters.IterativeFilter import ConvolutionStrategy;
from com.deconware.algorithms.fft.filters.IterativeFilter import AccelerationStrategy;

from net.imglib2.type.numeric.real import FloatType

jythondir="/home/bnorthan/Brian2014/Projects/deconware2/deconware-scripts/jython/"

phantomdir=jythondir+"phantom/"
experimentdir=phantomdir+"experiments/"
psfdir=jythondir+"psf/"

sys.path.append(phantomdir)
sys.path.append(experimentdir)
sys.path.append(psfdir)

import MultiChannelPhantom
reload(MultiChannelPhantom)
#import CreatePsf
#reload(CreatePsf)

from MultiChannelPhantom import MakeMultiChannelPhantom
#from CreatePsf import CreatePsf

import  Spheres2
reload(Spheres2)
from Spheres2 import Spheres2

xsize=128
ysize=128
zsize=64

xsizepsf=128
ysizepsf=128
zsizepsf=128

extensionxy=10
extensionz=20

size=[128, 128, 64]
psfsize=[128, 128, 128]
extendedsize=map(operator.add, size, psfsize)

print extendedsize

spheres=Spheres2(size[0], size[1], size[2], psfsize[0], psfsize[1], psfsize[2], 1, "", ops)

#create the phantom
phantom = spheres.CreatePhantom()
# create the phantom
#phantom=MakeMultiChannelPhantom(ops, size)
#MakeMultiChannelPhantom([256, 256, 128, 5])
display.createDisplay("phantom",  data.create(phantom));

# create the psf
psf = ops.run("psf", psfsize[0], psfsize[2], [100, 100, 300], 400, 1.4, 1.51, 1.51, 10)
display.createDisplay("psf",  data.create(psf));

#extended = ops.run("extend", None, phantom, extensionxy, extensionz, BoundaryType.ZERO, FFTTarget.MINES_SPEED)
extended = ops.run("extend", None, phantom, spheres.objectSizeX, spheres.objectSizeY, spheres.objectSizeZ, ExtensionType.DIMENSION, BoundaryType.ZERO, FFTTarget.MINES_SPEED)
display.createDisplay("extended",  data.create(extended));

background=FloatType()
background.setReal(0.0001)
ops.run("add", extended, background)

extendedPsf = ops.run("extend", None, psf, spheres.objectSizeX, spheres.objectSizeY, spheres.objectSizeZ, ExtensionType.DIMENSION, BoundaryType.ZERO, FFTTarget.MINES_SPEED)
#extendedPsf = ops.run("extend", None, psf, extensionxy, 0, BoundaryType.ZERO, FFTTarget.MINES_SPEED)
display.createDisplay("extended psf",  data.create(extendedPsf));

# convolve
convolved=ops.run("frequencyfilter", extended, extendedPsf, ConvolutionRaiRai())
display.createDisplay("convolved",  data.create(convolved))

extendedDimensions=[]
for i in range(0,3):
	extendedDimensions.append(extended.dimension(i))

print extendedDimensions

# crop

# extend again

# deconvolve
deconvolved=ops.create(extendedDimensions, FloatType());
#ops.run("richardsonlucy", convolved, psf, deconvolved, 2, AccelerationStrategy.MULTIPLICATIVE_VECTOR, ConvolutionStrategy.SEMI_NONCIRCULANT, 50, 60, 70);

ops.run("richardsonlucy", convolved, extendedPsf, deconvolved, 10, AccelerationStrategy.MULTIPLICATIVE_VECTOR, ConvolutionStrategy.CIRCULANT, 128, 128, 64);
display.createDisplay("deconvolved", data.create(deconvolved))'''
