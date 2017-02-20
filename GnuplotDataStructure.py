"""
The package GnuplotDataStructure will read a datafile containing datasets and datablocks, and returns them as numpy arrays.
"""

import numpy as np
from StringIO import StringIO
import matplotlib.pyplot as plt


class GnuplotDataStructure:
    """

    Members:

        'gnuplot' -- the file object gathering the commands.

    Methods:

        '__init__' -- print activation information.

        'parseDatafile' -- read gnuplot datafile and parse it to numpy arrays.

        'plotData' -- plot the parsed data.

    """
    
    def __init__(self):
        print('GnuplotDataStructure objects can be created')

    def parseDatafile(self, filename, index, block):
        f = open(filename, 'r')
        raw_data = f.read()
        f.close()

        dataset = raw_data.split('\n\n\n')
        datablock = dataset[index].split('\n\n')
        part = StringIO(datablock[block])
        return np.loadtxt(part)

    def plotData(self, filename, index, block, x, y):
        data = self.parseDatafile(filename, index, block)
        plt.plot(data[:,x], data[:,y])
        plt.show()
