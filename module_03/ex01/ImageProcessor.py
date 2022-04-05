import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt


class ImageProcessor:
    def load(self, path):
        """Opens the .png file and return
        array with the RGB values
        Must display a message specifying the dimensions"""
        try:
            file = img.imread(path)
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
            plt.imshow(array)
            plt.show()
        except AttributeError:
            print("Error")
            return
        
        