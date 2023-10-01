import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# 垂直拼接和水平拼接
v_arr = np.vstack((arr1, arr2))
h_arr = np.hstack((arr1, arr2))

print(v_arr)
print(h_arr)
# 初始化为0和1
print(np.zeros((1, 3)))
print(np.ones((1, 3)))

# 创建一个对角线为1的正方形矩阵
print(np.eye(3))

# 获取0轴上的最大值索引
np.argmax(arr1, axis=0)