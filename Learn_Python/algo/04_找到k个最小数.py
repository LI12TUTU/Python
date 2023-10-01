# 分治也是采用类快排的思想来做

[length, k] = [int(num) for num in input().split()]
arr = [int(num) for num in input().split()]

arr.sort()
print(arr[k - 1])
