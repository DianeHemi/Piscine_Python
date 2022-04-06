import numpy as np


class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        Authorized functions:None
        Authorized operator:+,-
        """
        if not isinstance(array, np.ndarray):
            return None
        
        array[:, :, :3] = 255 - array[:, :, :3]
        return array
        
        
        
    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        Authorized functions:.zeros,.shape,.dstack
        Authorized operator:None
        """
        if not isinstance(array, np.ndarray):
            return None

        if array.shape[2] == 4:
            ret = np.dstack((np.zeros(np.shape(array[:, :, 1])), 
                            np.zeros(np.shape(array[:, :, 1])), 
                            array[:, :, 2], 
                            array[:, :, 3]))
        else :
            ret = np.dstack((np.zeros(np.shape(array[:, :, 1])), 
                            np.zeros(np.shape(array[:, :, 1])), 
                            array[:, :, 2]))
        return ret
        
        
    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        Authorized functions:copy.deepcopy
        Authorized operator:*
        """
        if not isinstance(array, np.ndarray):
            return None
        
        green = array.copy()
        green[:, :, 0] = 0
        green[:, :, 2] = 0
        return green
        
        
    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        Authorized functions:.to_green,.to_blue
        Authorized operator:-,+
        """
        if not isinstance(array, np.ndarray):
            return None
        
        g = self.to_green(array)
        b = self.to_blue(array)
        
        ret = (g + b) - array
        return ret
        
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args:
            array: numpy.ndarray corresponding to the image.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        Authorized functions:.arange,.linspace
        """
        new = np.array(array)
        shades = np.linspace(0, 255, num=4, endpoint=False, dtype='uint8')
        for value in shades:
            new[array >= value] = value
        
        return new
        
        
        
    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in ['m','mean','w','weight']
            weights: [kwargs] list of 3 floats where the sum equals to 1,
            corresponding to the weights of each RBG channels.
        Return:
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
            This function should not raise any Exception.
        Authorized functions:.sum,.shape,.tile,.reshape,.dstack,.broadcast_to,.as_type
        Authorized operator:*,/
        """
        if filter is "mean" or filter is "m":
            new = np.sum(array[:, :, :3], axis=2) / 3
            new = np.dstack((new, new, new))
            return new
        elif filter is "weight" or filter is "w":
            for element in kwargs:
                values = list(kwargs[element])
            if np.sum(values) != 1.0:
                return None
            
            if array.shape[2] == 4:
                new = np.dstack((array[:, :, 0] * values[0], array[:, :, 1] * values[1], array[:, :, 2] * values[2], array[:, :, 3]))
            else:
                new = np.dstack((array[:, :, 0] * values[0], array[:, :, 1] * values[1], array[:, :, 2] * values[2]))
            return new
        else:
            return None
        
        