length = int(input())
nums = input().split()
for i in range(length):
	if nums.count(nums[i]) >= length / 2:
		print(nums[i])
		break
