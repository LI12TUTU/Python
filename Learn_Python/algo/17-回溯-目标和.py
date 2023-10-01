res = []
subset = []

def backtracking(nums, target, startIndex):
  subsetSum = sum(subset)
  if subsetSum == target and len(subset) == len(nums):
    res.append(subset[:])
    return
  
  if startIndex > len(nums) - 1:
    return
  
  # 先加-号
  subset.append(-nums[startIndex])
  backtracking(nums, target, startIndex + 1)
  subset.pop()
  # 回溯时再加+号
  subset.append(+nums[startIndex])
  backtracking(nums, target, startIndex + 1)
  subset.pop()


nums = [int(num) for num in input().split()]
target = int(input())
backtracking(nums, target, 0)
print(len(res))