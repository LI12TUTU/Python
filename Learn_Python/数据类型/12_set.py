num_set = {1, 2, 3, 4, 5, 6}
empty_set = set()

# 不支持下标索引 可修改
num_set.add(7)
num_set.remove(1)
num = num_set.pop() # 随机取出集合中的元素
num_set.clear()

num_set2 = {3, 2, 5, 7, 8}
# 取差集
set3 = num_set.difference(num_set2)
# 删除集合1中和集合2的重复元素
num_set.difference_update(num_set2)
set4 = num_set.union(num_set2)

len(num_set)
for el in num_set:
	print(el)

