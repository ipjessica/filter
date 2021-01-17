# Filter
A filter that extracts certain features of an image via kernels in a convolutional neural network.   
  
A kernel is a 2-D matrix of weights that moves over the input and performs dot product operations with the regions in the input image. The output of which is a representation of a number between 0 and 255. In a grayscale image, that number corresponds to the brightness of one pixel in the image.  
  
The filter itself is a 3-D structure of the kernels stacked together that produces the output with the desired features extracted.
