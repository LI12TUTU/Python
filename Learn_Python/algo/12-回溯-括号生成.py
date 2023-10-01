def gengerate_bracket(n):
    res = []

    """
    l: 左括号的数量
    r: 右括号的数量
    "" 0 0
    "(" 1 0
    "((" 2 0
    "(((" 3 0
    "(((" 4 0 return
    "((()" 3 1
    "((()" 4 1 return
    "((())" 3 2
    "((())" 4 2 return
    "((()))" 3 3 res = ["((()))"]
    "((()))" 4 3 return
    "((()))" 3 4 return
  """

    def dfs(str, l, r):
        # 左括号数量要大于右括号数量 否则不符合
        # 左括号和右括号数量大于n 搜索结束
        if r > l or l > n or r > n:
            return
        # 左右括号数量相等 搜索到一个结果
        if l == n and r == n:
            res.append(str)
            return
        # 左括号优先搜索
        dfs(str + "(", l + 1, r)
        dfs(str + ")", l, r + 1)

    dfs("", 0, 0)

    return res


n = int(input())
res = gengerate_bracket(n)
print(str(res).replace("'", ""))
