import math
import sys

from PIL import Image, ImageFilter

# ensure correct usage
if len(sys.argv) != 2:
    sys.exit("Usage: python filter.py filename")

# open image
image = Image.open(sys.argv[1]).convert("RGB")

"""
size - kernel size, given as (width, height); must be (3, 3) or (5, 5)
scale - can be none, meaning the default is the sum of the kernel weights; 
        if given, the result for each pixel is divided by this value
offset - if given, this value is added to the result after it has been divided by the scale

scale affects the outcome's brightness:
bright-----------------------------------normal-----------------------------------dark
0--1/100--------------1/2------------------1-----------10-----------50-------------100(and negative values)
"""

# edge detection kernel - shows large differences in pixel values. 
# pixels next to those whose values differ greatly will appear white; black if the values are similar
"""filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
    scale=1
))"""

# gaussian blur - minimizes the differences in pixel values
"""filtered = image.filter(ImageFilter.Kernel(
    size= (5,5),
    kernel=[1/256, 4/256, 6/256, 4/256, 1/256,
            4/256, 16/256, 24/256, 16/256, 4/256,
            6/256, 24/256, 36/256, 24/256, 6/256,
            4/256, 16/256, 24/256, 16/256, 4/256,
            1/256, 4/256, 6/256, 4/256, 1/256],
    scale=1
))"""

# shift by one pixel to the left -
# resulting unwanted border can be eliminated with zero padding, edge value replications, 
# amongst other techniques
"""filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[0, 0, 0, 1, 0, 0, 0, 0, 0],
    scale=1
))"""

# sharpen (can be broken down into two steps) - 
# takes a smoothed image, subtracts it from the original to obtain the details,
# then adds the details to the original
"""original = [0, 0, 0, 0, 1, 0, 0, 0, 0]
   smoothed = [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
   details = [0, 0, 0, 0, 1, 0, 0, 0, 0] - [1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9]
1. original - smoothed = details
2. original + details = sharpened"""
filtered = image.filter(ImageFilter.Kernel(
    size=(3, 3),
    kernel=[-1/9, -1/9, -1/9, -1/9, 17/9, -1/9, -1/9, -1/9, -1/9],
    scale=1
))

# show resulting image
filtered.show()
