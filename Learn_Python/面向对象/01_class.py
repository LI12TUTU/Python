class Person:
	name = None
	age = None
	# 私有变量
	__friend = None
	# 私有方法
	def __show_friend(self):
		print(self.__friend)

	# 构造方法
	def __init__(self, name):
		self.name = name

	# Person类型转换成字符串时调用的方法
	def __str__(self):
		return self.name

	def __lt__(self, other):
		return self.age < other.age

	def __le__(self, other):
		return self.age <= other.age

	def __eq__(self, other):
		return self.age == other.age

	def show_message(self):
		print(self.name)

# 继承 可以多继承 在(父类1，父类2，...) 多继承按从左到右继承 出现同名时保留左边的 左边的优先
class Student(Person):
	pass # 只继承父类不定义新的内容 使用pass关键字

class Teacher(Person):
	def show_message(self):
		Person.show_message(self)
		super().show_message()
		print("hhh")


s = Person()
s.name = 'lru'
s.show_message()
print(s, str(s))
