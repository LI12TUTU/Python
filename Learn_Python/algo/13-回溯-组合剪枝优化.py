res = []
num_list = []

def backtracking(n, k, start_index):

  if (len(num_list) == k):
    res.append(num_list[:])
    return
  
  # 剪枝优化
  # 1 2 3 4 选4个元素
  # 第一层for循环时从2开始遍历已经没有意义
  # n - (k - remain_size) + 1 终止的遍历索引
  for i in range(start_index, n - (k - len(num_list)) + 1 + 1):
    num_list.append(i)
    backtracking(n, k, i + 1)
    num_list.pop()

[n, k] = [int(num) for num in input().split()]
backtracking(n, k, 1)
print(str(res))