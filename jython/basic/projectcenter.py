# @ImagePlus imp

from ij import IJ

IJ.run(imp, "Reslice [/]...", "output=1.000 start=Top avoid");

imp.setSlice(65)
imp.update()