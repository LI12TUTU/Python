res = []
subset = []


def backtracking(targetSum, targetIndex, startIndex):
  subsetSum = sum(subset)
  if subsetSum > targetSum:
    return
  
  if len(subset) == targetIndex:
    if subsetSum == targetSum:
      res.append(subset[:])
    return

  for i in range(startIndex, 10):
    subset.append(i)
    backtracking(targetSum, targetIndex, i + 1)
    subset.pop()

[targetIndex, targetSum] = [int(num) for num in input().split()]
backtracking(targetSum, targetIndex, 1)
print(res)