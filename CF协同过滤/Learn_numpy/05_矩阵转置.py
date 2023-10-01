import numpy as np

arr = np.arange(24).reshape((4, 6))
a1 = arr.transpose()
print(a1)
a2 = arr.T
a3 = arr.swapaxes(1, 0)
print(a2, a3)