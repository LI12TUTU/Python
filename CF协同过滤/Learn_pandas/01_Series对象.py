import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3], index=list([1, 2, 3]))
print(list(s.sort_values(ascending=False)[0:2].index))
# print(s[0:2], type(s[0:2]), s[0:2].index, list(s[0:2].index))


# print(np.zeros(10))
# print(np.arange(1, 10))
s1 = pd.Series(np.zeros((10,)), index=np.arange(1, 11))
# print(s1)
# print(s, type(s), s[1])
# print(s.index, type(s.index))
# # 可遍历
# for i in s.index:
# 	print(s[i])
# print(s.values)
# print(type(s.values))

dict1 = {
	"name": "lll",
	"age": 18
}

# 访问和ndarray类似
# s1 = pd.Series(dict1)
# print(s1)

