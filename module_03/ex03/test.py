from ImageProcessor import ImageProcessor
from ColorFilter import ColorFilter


imp = ImageProcessor()
arr = imp.load("elon_canaGAN.png")
#arr = imp.load("../ex01/42AI.png")
#imp.display(arr)
# Output
# Loading image of dimensions 200 x 200

cf = ColorFilter()

#imp.display(cf.to_green(arr))
#imp.display(cf.invert(arr))
#imp.display(cf.to_blue(arr))
#imp.display(cf.to_red(arr))
#imp.display(cf.to_celluloid(arr))
#imp.display(cf.to_grayscale(arr, 'm'))

imp.display(cf.to_grayscale(arr, 'weight', weigth=[0.2, 0.5, 0.3]))