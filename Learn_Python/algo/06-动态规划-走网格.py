def walk_net(row, column):
  # 定义状态
  dp = [[i for i in range(column)] for j in range(row)]
  # 初始化状态
  dp[0][0] = 0
  # 第一行和第一列肯定只有一种走法
  for i in range(1, column):
    dp[0][i] = 1
  for i in range(1, row):
    dp[i][0] = 1

  for i in range(1, row):
    for j in range(1, column):
      # 状态转移方程 每种状态只能从上面或者左边过来 等于上面和左边的走法和
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
  
  return dp[row - 1][column - 1]

[row, column] = [int(n) for n in input().split()]
print(walk_net(row, column))


