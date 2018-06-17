from ctypes import *
import ctypes.util  
from numpy.ctypeslib import ndpointer 
import numpy as np
from numpy.random import *

lib = np.ctypeslib.load_library("libadd.so",".")

row = 20
col = 5
n = 5

matrix = rand(row, col)

_DOUBLE_PP = ndpointer(dtype=np.uintp, ndim=1, flags='C')

lib.add_matrix.argtypes = [_DOUBLE_PP, c_int32, c_int32, c_int32]
lib.add_matrix.restype = None

tp = np.uintp
mpp = (matrix.__array_interface__['data'][0] + np.arange(matrix.shape[0])*matrix.strides[0]).astype(tp)

n = ctypes.c_int(n)
row = ctypes.c_int(row)
col = ctypes.c_int(col)

print("before:", matrix)

lib.add_matrix(mpp, row, col, n)

print("after:", matrix)
