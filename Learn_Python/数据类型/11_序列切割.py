# 可以对列表 元组 字符串进行切片操作 即切割序列的部分成为子序列

num_list = [1, 2, 3, 4, 5, 6]
res = num_list[1:4:2]
print(res)

num_tuple = (1, 2, 3, 4, 5, 6)
# 不写默认从头截到尾
res1 = num_tuple[:]

str1 = "helloworld"
# 负数为从后往前取
res2 = str1[::-1]