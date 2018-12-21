import matplotlib.pyplot as plt

values = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6, 10]
plt.hist(values, bins=3)
plt.show()
plt.clf()
# by default number of bins is 10
plt.hist(values)
plt.show()
