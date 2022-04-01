import random
from typing import Iterable
import numpy as np
import warnings


class NumPyCreator:
    def from_list(self, lst):
        if not isinstance(lst, list):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.array(lst)
        except Exception:
            return None


    def from_tuple(self, tpl):
        if not isinstance(tpl, tuple):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.array(tpl)
        except Exception:
            return None
     
        
    def from_iterable(self, itr):
        if not isinstance(itr, Iterable):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.array(itr)
        except Exception:
            return None
        
        
    def from_shape(self, shape, value=0):
        if not isinstance(shape, tuple) or not isinstance(value, int):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.full(shape, value)
        except Exception:
            return None
        
        
    def random(self, shape):
        if not isinstance(shape, tuple):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.random.randn(shape[0], shape[1])
        except Exception:
            return None
        
    def identity(self, n):
        if not isinstance(n, int):
            return None
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("error")
                return np.identity(n)
        except Exception:
            return None
        