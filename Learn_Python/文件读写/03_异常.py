try:
	num = 4 / 0
# except:
# 	print("exception")
except ZeroDivisionError as e:
	print("Zero", e)
except (NameError, ZeroDivisionError) as e:
	print("Error")
except Exception as e:
	print("Exception")
# 没有出现异常执行
else:
	print("right")
finally:
	print("over")