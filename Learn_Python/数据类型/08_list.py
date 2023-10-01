# list类似于数组 访问可通过下标访问

name_list = ["lry", "zzy", "zcy"]
print(name_list)

mix_list = [1, "1", True]
embed_list = [[1, 2, 3], ["1", "2"]]

print(mix_list)
print(embed_list)

name_list.index("lry")
name_list.insert(0, "lll")
name_list.append("lku")
name_list.extend(["lru", "ljs"])

del name_list[0]
name_list.pop(2)
name_list.remove("lry")
name_list.clear()
name_list.count("lry")
len(name_list)

index = 0
while index < len(name_list):
	print(name_list[index])
	index += 1

for el in name_list:
	print(el)