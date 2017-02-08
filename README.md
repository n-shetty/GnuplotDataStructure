# GnuplotDataStructure

The structure of datafile expected by gnuplot has datasets and datablocks. Multiple datasets can be present in the same file. And each dataset can have multiple datablocks. Two datasets are separated by two blank lines, and two datablocks are separated by a single blank line.


In gnuplot, a dataset can be chosen by invoking the keyword "index", and a datablock can be chosen by invoking the keyword "every". Below is a sample gnuplot command illustrating their usage.

plot 'sample.dat' index 0 every :::0::0  using 1:3

The above command plots the data contained in the first dataset (as indicated by "index 0") and in the first datablock (as indicated by every :::0::0).

For further info on "index" and "every" please refer to the gnuplot manual.

The package GnuplotDataStructure will read a datafile containing datasets and datablocks, and converts them to numpy arrays. The data contained in the newly created arrays can be plotted using matplotlib while conveniently choosing the dataset or datablock.

The methods in the class can parse and plot the data.

