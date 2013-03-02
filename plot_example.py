import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize.minpack import fsolve
from numpy.lib.function_base import interp
import data
from data import get_intersection_point

buy_prices, buy_volumes = data.get_data('2011-01-01 00:00:00', '2011-01-01 00:00:00', prices='buy')
sell_prices, sell_volumes = data.get_data('2011-01-01 00:00:00', '2011-01-01 00:00:00', prices='sell')

for i in range(0, len(buy_prices)):
    
    x_buy = [r for r in buy_volumes[i]]
    y_buy = [r for r in buy_prices[i]]

    x_sell = [r for r in sell_volumes[i]]
    y_sell = [r for r in sell_prices[i]]

    f_buy = lambda x: interp(x, x_buy, y_buy)
    f_sell = lambda x: interp(x, x_sell, y_sell)
   
    intersect_x = fsolve(lambda x : f_sell(x) - f_buy(x), 10000)
    
    #plt.plot(x_buy, f_buy(x_buy), 'g.')
    #plt.plot(x_sell, f_sell(x_sell), 'b.')
    
    intersect_x, intersect_y = get_intersection_point(x_buy, y_buy, x_sell, y_sell)
    
    plt.plot(intersect_x, intersect_y, 'rx')
    
plt.yticks(np.arange(-200, 2000, 100.0))
plt.xticks(np.arange(20000, 55001, 5000))
plt.grid()
plt.show()