import matplotlib.pyplot as plt
import numpy as np

year = [i + 1940 for i in range(101)]
population = [np.round(np.sqrt(i), 10) + 7 for i in range(101)]

plt.plot(year, population)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projections')
plt.yticks([0, 5, 10, 15, 20], ['0', '5B', '10B', '15B', '20B'])

plt.show()

year = [1910, 1920, 1930] + year
population = [1.0, 2.5, 2.9] + population

plt.plot(year, population)
plt.fill_between(year, population, 0, color='blue')
plt.text(1910, -0.5, 'Min')
plt.text(2040, 17, 'Max')
plt.grid(True)

plt.show()
