num_list = [1, 2, 3, 4]

length = len(num_list)
max_el = max(num_list)
min_el = min(num_list)

obj = {
	"name": "lrl",
	"age": 18
}

list(obj) # 转成list 只保留key
set(obj)
tuple(obj)
str(obj) # 直接转成字符串
# 对容器进行排序 并转成列表 加上后面参数为逆序
sorted(num_list, reverse = True)