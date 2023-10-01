def max_common_length(str1, str2):
  res_max_length = 0

  # 第一个字串以某一个字符开头的最长字串
  for i in range(len(str1)):
  
    curr_max_length = 0
    prev = 0

    for j in range(i, len(str1)):
      for k in range(prev, len(str2)):
        if str2[k] == str1[j]:
          curr_max_length += 1
          # 从第二个字串的下一个位置开始扫描
          prev = k + 1
          break
    
    res_max_length = max(res_max_length, curr_max_length)

  return res_max_length

str = input().split()
print(max_common_length(str[0], str[1]))