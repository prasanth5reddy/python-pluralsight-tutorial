import numpy as np

height = np.round(np.random.normal(1.75, 0.20, 100), 2)
weight = np.round(np.random.normal(60.32, 15, 100), 2)

np_city = np.column_stack((height, weight))

print(np.mean(np_city[:, 0]))
print(np.median(np_city[:, 1]))
print(np.corrcoef(np_city[:, 0], np_city[:, 1]))
print(np.std(np_city[:, 0]))
