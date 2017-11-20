import numpy as np
import nitroplot

# example based on
# http://matplotlib.org/examples/pylab_examples/major_minor_demo2.html

active_sheet("sine")

t = np.arange(0.0, 75.0, 0.1)

s = np.sin(np.pi*t)*np.exp(-t*0.05)

Cell("P2").vertical = t
Cell("Q2").vertical = s

nitroplot.plot(t, s)
nitroplot.graph()





