res = []
subset = []

def backtracking(str, startIndex):

  if startIndex == len(str):
    res.append(subset[:])
    return
  
  for i in range(startIndex, len(str)):
    substr = str[startIndex:i + 1]
    reversedStr = substr[::-1]
    # 不是回文串，截取失败，尝试另一种截取方案
    if reversedStr != substr:
      continue
    subset.append(substr)
    backtracking(str, i + 1)
    # 回溯时，尝试下一种截取方案
    subset.pop()

string = input()
backtracking(string, 0)
print(str(res).replace("'", ""))