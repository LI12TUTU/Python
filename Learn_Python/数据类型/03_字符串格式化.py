name = "lry"
age = 18
height = 171.5

# 占位符 %s 将变量转为字符串
message = "%s年龄%d身高%.2f" % (name, age, height)

print(message)
# 字符串拼接 f标记 format
print(f"{name}age{age}height{height}")