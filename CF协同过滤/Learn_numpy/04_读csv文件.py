import numpy as np

# usecols skiprows dtype delimiter unpack
data = np.loadtxt("../ratings.csv", skiprows=1, dtype="int")

print(data, type(data))

# ndarray 支持下标 切片
# 取指定行
print(data[[2, 4, 6]])
# 取列
print(data[[1], [1,2]])

# 大于20的值全部赋值为0
data[data > 20] = 0
# 三元运算 大于20的赋值为0 否则为20
np.where(data > 20, 0 ,20)
# 小于10的替换成10 大于18的替换成18 nan不会被操作
np.clip(10, 18)