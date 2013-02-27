import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline 
from numpy.lib.function_base import interp
from numpy.core.function_base import linspace

# given values
'''xi = np.array([0.2, 0.5, 0.7, 0.9])
yi = np.array([0.3, -0.1, 0.2, 0.1])
# positions to inter/extrapolate
x = np.linspace(0,1,50)
# spline order: 1 linear, 2 quadratic, 3 cubic ... 
order = 1 
# do inter/extrapolation
s = InterpolatedUnivariateSpline(xi, yi, k=order)
y = s(x)

# example showing the interpolation for linear, quadratic and cubic interpolation
plt.figure()
plt.plot(xi,yi)
for order in range(1,4):
    s = InterpolatedUnivariateSpline(xi, yi, k=order)
    y = s(x)
    plt.plot(x,y)
plt.show()
'''


xp = [1,2,3,4,5]
fp = [1,4,9,16,25]
x = linspace(1,5, 100)

#f = interp(x, xp, fp)
f = lambda x: interp(x, xp, fp, left=999.0, right=-999.0)
print(f([4,5,6]))