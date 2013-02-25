'''
Created on Feb 19, 2013

@author: martin
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate.interpolate import interp1d

import time
from matplotlib.pyplot import draw, ion, plot
from numpy.core.numeric import arange
from numpy.ma.core import sin
from scipy.constants.constants import pi

ion() 
tstart = time.time()               # for profiling
x_buy = arange(0,2*pi,0.01)            # x_buy-array
line, = plot(x_buy,sin(x_buy))
for i in arange(1,200):
     line.set_ydata(sin(x_buy+i/10.0))  # update the data
     draw()                         # redraw the canvas
print('FPS:' , 200/(time.time()-tstart))
