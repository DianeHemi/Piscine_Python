from ScrapBooker import ScrapBooker
import numpy as np


spb = ScrapBooker()
arr1 = np.arange(0,25).reshape(5,5)
spb.crop(arr1, (3,1),(1,0))


arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
spb.thin(arr2,3,1)


arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print(spb.juxtapose(arr3, 3, 1))

arr = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
spb.mosaic(arr3, (3,3))