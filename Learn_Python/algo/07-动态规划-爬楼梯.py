def jump(n):
  # 每次跳1阶或2阶 因此状态i只可能来自于状态i - 1或状态i - 2的可能性之和
  # 跳到i - 2状态的方法
  # 初始化为1 为了方便计算
  prev = 1
  # 跳到i - 1状态的方法
  # 跳到1阶只有一种方法
  curr = 1
  next = 0

  for i in range(2, n + 1):
    next = prev + curr
    prev = curr
    curr = next

  # 跳到n阶时，curr保存了这个状态
  return curr

n = int(input())
print(jump(n))