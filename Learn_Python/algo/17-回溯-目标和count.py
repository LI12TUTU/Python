count = 0

def backtracking(nums, target, startIndex, sum):
  global count
  
  if sum == target and startIndex == len(nums):
    count += 1
    return
  
  if startIndex > len(nums) - 1:
    return
  
  backtracking(nums, target, startIndex + 1, sum - nums[startIndex])
  backtracking(nums, target, startIndex + 1, sum + nums[startIndex])


nums = [int(num) for num in input().split()]
target = int(input())
backtracking(nums, target, 0, 0)
print(count)