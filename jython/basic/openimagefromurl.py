# @DatasetService data
# @DisplayService display
# @IOService io
# @OpService ops

# define a local directory to get the images from
directory="/home/bnorthan/Brian2014/Images/TempForEasyAccess/"

# use 2-channels of the lena image for test image
image1Name="lena_red_32.tif"
image2Name="lena_green_32.tif"

# open first image
image1=data.open(directory+image1Name)

dataset=data.open("http://rsb.info.nih.gov/ij/images/blobs.gif")