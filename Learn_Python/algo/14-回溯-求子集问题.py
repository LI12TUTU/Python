res = []
subset = []

def backtracking(nums, startIndex):
  res.append(subset[:])
  if startIndex >= len(nums):
    return

  for i in range(startIndex, len(nums)):
    subset.append(nums[i])
    backtracking(nums, i + 1)
    subset.pop()

nums = [int(num) for num in input().split()]
backtracking(nums, 0)
print(res)
