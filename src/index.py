#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from histogram_viewer_3D import Hist3D as HV3

file = '/Users/richard/analysis/matlab/input/1606-0902-69_input/1606-0902-69-am241_190314_135115.hxt'

# Open raw data
raw = open(file, 'r+b')

# Skip 180 bytes of data
skip = raw.read(172)

# Read nRows
nRows_encoded = raw.read(4)
nRows = int.from_bytes(nRows_encoded,'little')

# Read nCols
nCols_encoded = raw.read(4)
nCols = int.from_bytes(nCols_encoded,'little')

# Read nBins
nBins_encoded = raw.read(4)
nBins = int.from_bytes(nBins_encoded,'little')

# Read the x-bins and decode them assuming
# little-endian ordering (<) and double precision
# floating point numbers (f8)
buffer = raw.read(nBins*8)
x_bins = np.frombuffer(buffer, dtype='<f8') # list

# Read and decode the spectrum for all pixels
buffer = raw.read(nBins*nCols*nRows*8)
y_bins = np.frombuffer(buffer, dtype='<f8') # list of length nBins*nCols*nRows


# Turn array into matrix
matrix= y_bins.reshape(nCols, nRows, nBins)

# View histogram

figure, axis = plt.subplots(1,1)
histogram_viewer = HV3(matrix, axis)
figure.canvas.mpl_connect('scroll_event', histogram_viewer.scroll)
plt.show()
