res = []
num_list = []

def backtracking(n, k, start_index):
  """
    start_index: 集合的起始索引
  """

  # 回溯终止条件 搜索到叶子节点 找到一个结果
  if (len(num_list) == k):
    # 拷贝数据 防止操作内存同一片地址导致结果出错
    res_list = []
    res_list.extend(num_list)
    res.append(res_list)
    return
  
  for i in range(start_index, n + 1):
    num_list.append(i)
    backtracking(n, k, i + 1)
    # 回溯 弹出当前元素
    num_list.pop()

[n, k] = [int(num) for num in input().split()]
backtracking(n, k, 1)
print(str(res))