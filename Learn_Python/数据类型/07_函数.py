# 没写返回值时默认返回None
# not == ! and == && or == ||
# in not in
# 函数也可以作为参数传递 回调函数
def my_len(str1):
	"""
	计算字符串长度
	:param str1: 字符串
	:return: 字符串长度
	"""
	count = 0
	for ch in str1:
		count += 1
	return count


num = 100


def change_num():
	global num
	num = 200
	print(num)


change_num()
print(num)

my_len("aaaaa")


# 多返回值？有啥用
def test():
	return 1, 2, 3


x, y, z = test()

# **kwargs 传参时以key value键值对形式传递 类型为字典
# *args剩余参数 接收所有剩余的参数 类型为元组
def test1(parm1, parm2, parm3=1, *args):
	print("test")


# 好乱 居然还可以直接指定传参
test1(parm2=1)
test1(2, parm3=1)


# 类似箭头函数把匿名函数
lambda x, y: x + y
