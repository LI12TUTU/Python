# key不可重复 字典不就是对象 一个哈希表？
# key可以为任意数据类型，但是不可以为对象 value可以为任意值
from operator import itemgetter

# obj = {
# 	"name": "lry",
# 	"age": 18,
# 	"height": 1.88
# }
#
# obj["friend"] = {
# 	"name": "zzy"
# }
# obj["age"] = 20
# height = obj.pop("height")
# # 获取对象的所有key
# keys = obj.keys()
# for key in keys:
# 	print(obj[key])
# for key in obj:
# 	print(obj[key])
# # 获取key的个数
# length = len(obj)
# obj.clear()
#
# print(obj["name"])

obj = {
	1: 10,
	3706: 20
}

print(obj.items())
print(sorted(obj.items(), key=itemgetter(1), reverse=True))
