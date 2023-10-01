res = []
subset = []

def backtracking(candidates, target, startIndex):
  subsetSum = sum(subset)

  if subsetSum > target:
    return

  if subsetSum == target:
    res.append(subset[:])
    return
  
  for i in range(startIndex, len(candidates)):
    # 防止解集中有重复的组合 已选取过的元素在回溯时不再选取
    if i > startIndex and candidates[i] == candidates[i - 1]:
      continue
    subset.append(candidates[i])
    backtracking(candidates, target, i + 1)
    subset.pop()

# candidates = [10,1,2,7,6,1,5]
# target = 8
candidates = [2, 5, 2, 1, 2]
target = 5
# 需要先对集合进行排序再去重
candidates.sort()
# [1, 2, 2, 2, 5]
backtracking(candidates, target, 0)
print(res)