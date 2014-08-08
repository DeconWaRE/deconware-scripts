# @DatasetService data
# @DisplayService display
# @net.imagej.ops.OpService ops

# define a local directory to get the images from
directory="/home/bnorthan/Brian2014/Images/TempForEasyAccess/"

# use 2-channels of the lena image for test image
image1Name="lena_red_32.tif"
image2Name="lena_green_32.tif"

# open first image
image1=data.open(directory+image1Name)
display.createDisplay(image1.getName(), image1)

# open second image
image2=data.open(directory+image2Name)
display.createDisplay(image2.getName(), image2);

# add the images
image3 = ops.add(image1,image2)
display.createDisplay(image3.getName(), image3)

#blobs=data.open("http://rsb.info.nih.gov/ij/images/blobs.gif")
#display.createDisplay(blobs.getName(), blobs)
