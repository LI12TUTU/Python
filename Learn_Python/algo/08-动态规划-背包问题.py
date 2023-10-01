def bag_problem(value, weight, count, bag_size):
  # dp 行表示物品i 列表示重量为j的背包 值表示重量为j的背包的最大价值（放入或不放入物品i）
  dp = [[0 for i in range(bag_size + 1)] for j in range(count)]
  current_size = 0

  # 初始化状态, 能放入第一件物品的背包价值
  for i in range(bag_size):
    if i - weight[0] < 0:
      dp[0][i] = 0
    else:
      dp[0][i] = value[0]
  # 初始化状态 重量为0的背包价值为0
  for i in range(count):
    dp[i][0] = 0
  

  for i in range(1, count):
    for j in range(1, bag_size + 1):
      # 放入物品i之后的背包重量
      current_size = j - weight[i]
      # 放不进去
      if current_size < 0:
        dp[i][j] = dp[i - 1][j]
      else:
        # 状态转移方程 取放入物品i之后和放入之前的最大价值和 以及 未放入之前的最大价值 两者之间的最大值
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][current_size] + value[i])

  return dp[count - 1][bag_size]

value = [42, 12, 40, 25]
weight = [7, 3, 4, 5]

[count, bag_size] = [int(n) for n in input().split()]
print(bag_problem(value, weight, count, bag_size))
