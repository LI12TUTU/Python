res = []
subset = []

def backtracking(nums, target, startIndex):
  subsetSum = sum(subset)
  
  if subsetSum == target:
    res.append(subset[:])
    return
  
  i = startIndex
  # 剪枝之前需要对数组进行排序
  # 否则当较大的元素在前时会搜索不到解
  while i < len(nums) and subsetSum + nums[i] <= target:
    subset.append(nums[i])
    backtracking(nums, target, i)
    subset.pop()
    i += 1

nums = [int(num) for num in input().split()]
target = int(input())
nums.sort()
backtracking(nums, target, 0)
print(res)