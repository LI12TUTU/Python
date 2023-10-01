# 导入time.py
# import time
# 从time模块导入sleep函数
# from time import sleep
# 导入所有功能
# 导入多个模块时名字重复后者会覆盖前者
from time import *
# import time as t
# import package1.module1 as m1
# m1.test()
from package1 import module1 as m1
m1.test()


sleep(10)
# time.sleep(10)