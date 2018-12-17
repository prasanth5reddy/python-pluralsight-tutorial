import numpy as np

height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]

np_2d = np.array([height, weight])

print(np_2d)
# print matrix order
print(np_2d.shape)

print(np_2d[0])

# below both prints same
print(np_2d[0][1], np_2d[0, 1])

# prints subset of matrix
print(np_2d[:, 1:3])

np_baseball = np.array([[75.2303559, 168.83775102, 23.99],
                        [75.02614252, 231.09732309, 35.69],
                        [73.1544228, 215.08167641, 31.78]])

print(np_baseball.shape)

conversion = np.array([0.0254, 0.453592, 1])

# note that numpy array product is not same as matrix multiplication
print(np_baseball * conversion)
