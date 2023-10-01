res = 0
subset = []

def backtracking(nums, startIndex):
  global res
  # 集合中只有一个元素 异或总和为其本身 空集异或总和为0 不做处理
  if len(subset) == 1:
    res += subset[0]
  
  if len(subset) > 1:
    XORsum = subset[0]
    # 求子集中的异或总和
    for i in range(1, len(subset)):
      XORsum = XORsum ^ subset[i]
    
    res += XORsum

  if startIndex >= len(nums):
    return

  for i in range(startIndex, len(nums)):
    subset.append(nums[i])
    backtracking(nums, i + 1)
    subset.pop()

nums = [int(num) for num in input().split()]
backtracking(nums, 0)
print(res)
