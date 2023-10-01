import numpy as np

arr = np.array([[1, 2, 3], [2, 3, 4]])
print(arr.shape)
# 可以像正常数组那样访问
for i in range(arr.shape[0]):
	for j in range(arr.shape[1]):
		print(arr[i][j])
# 改变数组的形状
arr1 = arr.reshape(3, 2)
print(arr.shape, arr1.shape, type(arr.shape))

arr2 = arr.reshape((arr1.shape[0] * arr1.shape[1],))
print(arr2)
# 数组降维
print(arr1.flatten())