import numpy as np

a = np.array([[1,2], [2,3], [6,7]])

b = a[np.where((a[0] > 1) & (a[1] < 7) & (a[1]< 5))]

print(b)