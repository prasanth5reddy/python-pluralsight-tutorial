import matplotlib.pyplot as plt
import numpy as np

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

plt.plot(year, pop)
plt.scatter(year, pop)
plt.show()

height = np.round(np.random.normal(1.75, 0.20, 100), 2)
weight = np.round(np.random.normal(60.32, 15, 100), 2)

plt.scatter(weight, height)
plt.xscale('log')
plt.show()
