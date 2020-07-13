
# The plot.hist() method takes in multiple arguments. Let’s look at a few important ones below:

# The first argument is the data set which is to be plotted
# Following are the optional arguments which may or may not be given:

# bins: This defines the number of intervals in the histogram

# range: This defines the range within which the number of bins should exist

# align: This takes in three possible values; left, mid, right and decides the position of the histogram in the image

# log: Set to true, this will return the log values of the scale for the histogram

# License: Creative Commons -Attribution -ShareAlike 4.0 (CC-BY-SA 4.0)


import matplotlib.pyplot as plot
import numpy as np

myList = np.random.normal(size = 1000)

plot.hist(myList, bins=20, align = 'mid') 

plot.ylabel('Probability')
plot.show()