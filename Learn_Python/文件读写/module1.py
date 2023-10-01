def test():
	print("test module")

# 运行时为主文件则执行 导入时不会执行
if __name__ == '__main__':
	test()

# 模块导出的内容
__all__ = ["test"]