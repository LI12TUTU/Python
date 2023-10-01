def longestPalindrome(str):
  length = len(str)
  # 只有一个字符时肯定为回文串, 直接返回
  if length < 2:
    return str
  # 最长的回文子串长度
  max_len = 1
  # 最长的回文子串长度起始索引
  begin = 0
  
  # dp[i][j] 代表str[i:j]是否为回文串
  dp = [[False for _ in range(length)] for _ in range(length)]
  # 初始化状态
  # 只有一个字符时肯定为回文串
  for i in range(length):
    dp[i][i] = True

  # 长度为n的子串是否为回文串
  for sub_len in range(2, length + 1):
    # 判断长度为n的子串是否为回文串
    for i in range(length):
      # 子串的右边索引 str[i:j]
      j = sub_len + i - 1
      curr_sub_len = j - i + 1
      # 越界 
      if j >= length:
        break
      # str[i]与str[j]不相等，一定不是回文串
      if str[i] != str[j]:
        dp[i][j] = False
      else:
        # 相等则判断子串长度小于3，小于3只要首尾字符一致一定是回文串
        if curr_sub_len <= 3:
          dp[i][j] = True
        # 子串长度大于3的回文串需要看str[i + 1:j - 1]是否为回文串
        else:
          dp[i][j] = dp[i + 1][j - 1]
      
      # 更新起始索引和最大长度
      if dp[i][j] and curr_sub_len > max_len:
        max_len = curr_sub_len
        begin = i
  
  return str[begin:begin + max_len]

str = input()
res = longestPalindrome(str)
print(res)
