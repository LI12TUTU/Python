numMap = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
res = []
subset = []

def backtracking(index, numStr):
    global subset
    global res

    if len(subset) == len(numStr):
        res.append("".join(subset))
        return
    num = numStr[index]
    numValue = numMap.get(num)
    for i in range(len(numValue)):
        subset.append(numValue[i])
        backtracking(index + 1, numStr)
        subset.pop()


backtracking(0, "23")
print(res)
