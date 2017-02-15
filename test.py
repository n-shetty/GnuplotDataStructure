from GnuplotDataStructure import GnuplotDataStructure as GP

file = "sample.dat"
index = 1
block = 1

data = GP().parseDatafile(file, index, block)

print data

