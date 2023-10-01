def longestCommonSubsequence(str1, str2):
  # dp[i][j] 代表str1[0:i - 1]和str2[0:j - 1]的最长公共子序列长度
  # 初始化状态 第一行和第一列均为0 和空串的最长公共子序列长度为0
  dp = [[0 for i in range(len(str2) + 1)] for i in range(len(str1) + 1)]

  for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
      # 状态转移方程 如果最后一个字符相同 长度加1
      if str1[i - 1] == str2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      # 如果最后一个字符不相同 取str1[0:i - 2]和str2[0: j - 1],str1[0:i - 1]和str2[0:j - 2]的最大值
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
  
  return dp[len(str1)][len(str2)]

[str1, str2] = input().split()
res = longestCommonSubsequence(str1, str2)
print(res)