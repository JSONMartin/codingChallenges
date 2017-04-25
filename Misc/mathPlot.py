#nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
#nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
#nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 66.6, 58.2, 52.0, 32.2]
import random
from pylab import plot, show, legend, title, xlabel, ylabel, axis

# randTemp = lambda: random.uniform(29, 80)

# months = range(1, 13)
# nyc_temp_2000 = [randTemp() for _ in range(1, 13)]
# nyc_temp_2006 = [randTemp() for _ in range(1, 13)]
# nyc_temp_2012 = [randTemp() for _ in range(1, 13)]

# print(nyc_temp_2000)
# plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012)
# title('Average temp in NYC')
# xlabel('Moth'); ylabel('Temperature')
# legend([2000, 2006, 2012])
# show()

nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 57.2, 49.2, 50.3]
plot(nyc_temp, marker='x')
axis()
plot()
axis(ymin=0)

show()