import numpy as np
import pandas as pd

t1 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list([1, 2, 3]), columns=list([1, 2, 3, 4]))
print(t1)
# print(t1.index)
# print(t1.columns, type(t1.columns))
# print(t1[0][0], t1[0][1], t1[1][0])
for i in t1.index:
	print(t1.loc[i])

for i in t1.index:
	for j in t1.columns:
		# print(t1[j][i])
		print(t1.loc[i, j])
		t1.loc[i, j] += 1

# iloc按位置来取数据 从0开始
print(t1.iloc[0, 0])
print(t1)
# for i in t1.index:
# 	print(i)
# 	print(t1[i])
# print("*" * 100)
# for i in t1.columns:
# 	print(i)
# 	print(t1[i])
# print(t1.values, type(t1.values))
# print(t1.shape, t1.dtypes)
# print(t1.head()) # 表格的前几行
# print(t1.tail()) # 表格的末几行
# print(t1.info())
# print(t1.describe())
# ascending=True or False 升序或降序排列 by=field 按哪个字段来排序
# print(t1.sort_values())
# t1.index 行索引
# t1.colums 列索引
# t1.values

# dict1 = {
# 	"name": ["lll", "yyy"],
# 	"age": [18, 20]
# }
# t2 = pd.DataFrame(dict1)
# print(t2)