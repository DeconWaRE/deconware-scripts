# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

# define a local directory to get the images from
directory="/home/bnorthan/Brian2014/Projects/deconware2/deconware-images/BasicTests/"

imageName="Bars_32_cropped.tif"
psfName="PSF-Bars_32_cropped.tif"

# open the image
image=data.open(directory+imageName)
display.createDisplay(image.getName(), image);	

# open the psf
psf=data.open(directory+psfName)
display.createDisplay(psf.getName(), psf);

# normalize the psf
ops.run("normalizesum", psf.getImgPlus())

# convolve
convolved=ops.run("Convolution", image.getImgPlus(), psf.getImgPlus())
display.createDisplay("convolved",  data.create(convolved));

# deconvolve
deconvolved=ops.run("RichardsonLucy", convolved, psf.getImgPlus(), 10)
display.createDisplay("deconvolved",  data.create(deconvolved));

# deconvolve using YacuDecu
yacudecu=ops.run("YacuDecu", convolved, psf.getImgPlus(), 10)
display.createDisplay("yacudecu",  data.create(yacudecu));