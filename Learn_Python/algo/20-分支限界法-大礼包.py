def shoppingOffers(price, needs, special):
    n = len(price)
    filterSpecial = []

    # 先过滤掉购买之后不合格的大礼包
    for sp in special:
        # 大礼包所购买的物品量大于0且大礼包的价格小于直接购买的价格
        if (
            sum(sp[i] for i in range(n)) > 0
            and sum(sp[i] * price[i] for i in range(n)) > sp[-1]
        ):
            filterSpecial.append(sp)

    def dfs(currNeeds):
        # 直接购买的价格
        minPrice = sum(need * price[i] for i, need in enumerate(currNeeds))
        # 遍历每一个大礼包
        for currSpecial in filterSpecial:
            specialPrice = currSpecial[-1]
            # 买了大礼包之后的购买需求
            nextNeeds = []
            # 判断大礼包是否可以买
            for i in range(n):
                # 大礼包包含的数量超过需求，不能购买
                if currSpecial[i] > currNeeds[i]:
                    break
                # 大礼包中i物品的数量不超过需求,可以购买,剩余需求下次递归购买
                nextNeeds.append(currNeeds[i] - currSpecial[i])
            # 大礼包中的物品数量不会超过需求,可以购买大礼包
            if len(nextNeeds) == n:
                minPrice = min(minPrice, dfs(tuple(nextNeeds)) + specialPrice)

        return minPrice

    return dfs(tuple(needs))


price = [int(n) for n in input().split()]

specialNum = price.pop()
special = []
for i in range(specialNum):
    gift = [int(n) for n in input().split()]
    special.append(gift)

needs = [int(n) for n in input().split()]
print(shoppingOffers(price, needs, special))
