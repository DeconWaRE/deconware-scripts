# @DatasetService data
# @DisplayService display
# @net.imagej.ops.OpService ops

blobs=data.open("http://rsb.info.nih.gov/ij/images/blobs.gif")
display.createDisplay(blobs.getName(), blobs)
