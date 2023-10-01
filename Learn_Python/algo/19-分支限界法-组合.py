num_list = []

def backtracking(n, k, start_index):

  if (len(num_list) == k):
    for i in range(len(num_list)):
      print(num_list[i], end=" ")
    print("")
    return
  
  for i in range(start_index, n - (k - len(num_list)) + 1 + 1):
    num_list.append(i)
    backtracking(n, k, i + 1)
    num_list.pop()

[n, k] = [int(num) for num in input().split()]
backtracking(n, k, 1)