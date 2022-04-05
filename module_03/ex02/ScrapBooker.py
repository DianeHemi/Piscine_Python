import numpy as np

class ScrapBooker:
    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Returns:
        new_arr: the cropped numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        
        new_array = array[position[0]:dim[0] + position[0], position[1]:dim[1] + position[1]]
        return new_array
        
        
        
        
    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Returns:
        new_arr: thined numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        if n < 0 or n > array.shape[0] or n > array.shape[1] or axis < 0 or axis > 1:
            return None
        
        if axis == 0:
            new_array = np.delete(array, slice(n - 1, None, n), 1)
        elif axis == 1:
            new_array = np.delete(array, slice(n - 1, None, n), 0)
        return new_array
        


        
        
    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Returns:
        new_arr: juxtaposed numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        new_array = array
        for i in range(n):
            new_array = np.concatenate((new_array, array), axis=axis)
        return new_array
        
        
        
        
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Returns:
        new_arr: mosaic numpy.ndarray.
        None otherwise (combinaison of parameters not incompatible).
        Raises:
        This function should not raise any Exception.
        """
        return np.tile(array, dim)
        
        