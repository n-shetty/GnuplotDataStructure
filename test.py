from GnuplotDataStructure import GnuplotDataStructure as GP

file = "sample.dat"
index = 1 # dataset
block = 1 # datablock

# columns
x = 0 # choose x axis
y = 1 # choose y axis

# parse data
data = GP().parseDatafile(file, index, block)

# plot data
GP().plotData(file, index, block, x, y)

print data

