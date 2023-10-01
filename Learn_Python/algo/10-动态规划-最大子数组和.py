def max_sub_array_sum(nums):
	pre_value = nums[0]
	max_sum = nums[0]

	for i in range(1, len(nums)):
		pre_value = max(nums[i], nums[i] + pre_value)
		max_sum = max(max_sum, pre_value)

	return max_sum


length = int(input())
nums = [int(num) for num in input().split()]
max_val = max_sub_array_sum(nums)
print(max_val)
