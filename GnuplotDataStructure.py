import numpy as np
from StringIO import StringIO

class GnuplotDataStructure:
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