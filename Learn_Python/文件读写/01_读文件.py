# r w a
import time

# 代码执行结束之后自动关闭文件
with open("./test.txt", "r", encoding="UTF-8") as file1:
	for line in file1:
		print(line)

file = open("./test.txt", "r", encoding="UTF-8")
print(file)
# read(num) 读取指定字节的内容
# content = file.read()
# print(content)
# 读取全部行 封装成list对象
# res = file.readlines()
# print(res)

# res = file.readline()
# file.close()
print(type(file))
for line in file:
	print(line)

time.sleep(5000)

