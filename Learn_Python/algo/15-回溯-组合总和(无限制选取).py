res = []
subset = []

def backtracking(nums, target, startIndex):
  subsetSum = sum(subset)
  if subsetSum > target:
    return
  
  if subsetSum == target:
    res.append(subset[:])
    return
  
  # startIndex 防止重复搜索已经出现过的解
  for i in range(startIndex, len(nums)):
    subset.append(nums[i])
    backtracking(nums, target, i)
    subset.pop()

backtracking([2, 3, 6, 7], 7, 0)
print(res)