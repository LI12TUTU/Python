def longest_palindrome(str):
  max_length = 0
  max_substr = ""

  for i in range(len(str)):
    for j in range(len(str)):
      origin_str = str[i:j + 1]
      reversed_str = origin_str[::-1]
      substr_length = len(origin_str)
      if origin_str ==  reversed_str and substr_length > max_length:
        max_substr = origin_str
        max_length = substr_length

  return max_substr

str = input()
res = longest_palindrome(str)
print(res)
