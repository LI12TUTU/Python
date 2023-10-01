import random

num = random.randint(1, 100)

print(num)

while num < 100:
	print("hhh")
	num += 1

"""
	range(n) 0 - n-1
	range(n, m) n - m-1
	range(n, m, step) step递增的大小
"""
for i in range(10):
	print(i)

for ch in "aaaa":
	print(ch)

for i in range(1, 10):
	for j in range(1, i + 1):
		print(f"{j} * {i} = {j * i}\t", end="")
	print()
