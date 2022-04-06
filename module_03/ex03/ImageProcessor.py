from locale import normalize
from pickletools import uint8
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


class ImageProcessor:
    def load(self, path):
        """Opens the .png file and return
        array with the RGB values
        Must display a message specifying the dimensions"""
        try:
            file = Image.open(path)
        except Exception:
            print("Error")
            return None
        
        self.array = np.array(file)
        print("Loading image of dimensions", self.array.shape[0], "x", self.array.shape[1])
        return self.array
        
        
    def display(self, array):
        """Takes a numpy array asargument
        displays the corresponding RGB image"""
        try:
            plt.imshow(array.astype('uint8'), vmin=0, vmax=255)
            plt.show()
        except AttributeError:
            print("Error")
            return
        
        