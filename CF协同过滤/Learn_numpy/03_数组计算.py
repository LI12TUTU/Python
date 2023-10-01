import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# 数组内所有元素执行运算
print(arr + 1)

arr1 = np.array([0, 2, 3, 4, 5])
print(arr + arr1)
print(arr1 / 0) # nan inf