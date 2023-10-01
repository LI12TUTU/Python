import numpy as np
import random

array1 = np.array([1,2,3])
print(array1, type(array1))

arr2 = np.array(range(5))
# 起始 结束 步长
arr3 = np.arange(1, 6, 2)
# dtype数组存放的数据类型
print(arr3, arr3.dtype)
# 指定数据类型
arr4 = np.array(range(1, 4), dtype=float)
print(arr4, arr4.dtype)

arr5 = arr4.astype("int64")
print(arr5.dtype)

arr6 = np.array([random.random() for i in range(10)])
# 保留小数 python也有这个函数
arr7 = np.round(arr6, 2)
# shape属性 数组的形状
print(arr7, arr7.shape)