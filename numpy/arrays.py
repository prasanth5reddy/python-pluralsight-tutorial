import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

# Following will give error
# bmi = weight / height ** 2

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2
print(bmi.round(2))

# multiple data types of list converts to only one data type in numpy array
print(np.array([1.0, 'is', True]))

# notice the difference
print(height + weight)
print(np_height + np_weight)

# access like normal lists
print(bmi[1])

print(bmi > 23)
# access bmi greater than 23
print(bmi[bmi > 23])
