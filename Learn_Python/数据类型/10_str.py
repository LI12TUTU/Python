# str也是只读 不可修改
str1 = "hello world"

str1.index("h")
# 不改变原字符串 得到一个新的字符串
str2 = str1.replace("hello", "HELLO")
# 得到一个list对象
str_list = str1.split(" ")

str3 = "    hello world   "
# 去除字符串首尾指定内容 默认为空格
str3.strip()
str2.count("hello")
len(str2)