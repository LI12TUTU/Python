[length, k] = [int(num) for num in input().split()]
arr = [int(num) for num in input().split()]

arr.sort(reverse=True)
print(arr[k - 1])