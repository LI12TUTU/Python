# 类快排
def quickSelect(nums, left, right, k):

  key = nums[left]
  i = left
  j = right

  while i < j:
    while i < j  and nums[j] > key:
      j -= 1
    nums[i] = nums[j]
    while i < j and nums[i] <= key:
      i += 1
    nums[j] = nums[i]
  
  # 快排一次划分 i指针和j指针均指向同一个位置 即该元素的最终位置
  nums[i] = key

  if k == i:
    return key
  
  # 若k下标小于该元素最终的位置，则目标元素在左子表中
  if k <= j:
    return quickSelect(nums, left, j, k)
  # 反之，若k下标大于该元素最终的位置，则目标元素在右子表中
  else:
    return quickSelect(nums, j + 1, right, k)
  
def findKthLargeset(nums, k):
  # len - k 第k个最大的元素在数组中的下标
  return quickSelect(nums, 0, len(nums) - 1, len(nums) - k)

[length, k] = [int(n) for n in input().split()]
nums = [int(num) for num in input().split()]
res = findKthLargeset(nums, k)
print(res)