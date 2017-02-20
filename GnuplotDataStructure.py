"""
The package GnuplotDataStructure will read a datafile containing datasets and datablocks, and returns them as numpy arrays.
"""

import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as plt


class GnuplotDataStructure:
    """

    Members:

        'file_handle' -- the file handle pointing to opened file
        'raw_data' -- holds the content of the file
        'dataset' -- holds datasets
        'datablock' -- holds datablocks
        'raw_datablock' -- lists are converted to raw data and held here
                           so as to be easily read back using numpy's loadtxt

    Methods:

        '__init__' -- print activation information.

        'parseDatafile' -- read gnuplot datafile and parse it to numpy arrays.

        'plotData' -- plot the parsed data.

    """
    
    def __init__(self):
        print('GnuplotDataStructure objects can be created')

    def parseDatafile(self, filename, index, block):
        file_handle = open(filename, 'r')
        raw_data = file_handle.read()
        file_handle.close()

        dataset = raw_data.split('\n\n\n')
        datablock = dataset[index].split('\n\n')
        raw_datablock = StringIO(datablock[block])
        return np.loadtxt(raw_datablock)

    def plotData(self, filename, index, block, x, y):
        data = self.parseDatafile(filename, index, block)
        plt.plot(data[:,x], data[:,y])
        plt.show()

        
