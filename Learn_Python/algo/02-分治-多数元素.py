"""
  思路

  如果数 a 是数组 nums 的众数，如果我们将 nums 分成两部分，那么 a 必定是至少一部分的众数。

  我们可以使用反证法来证明这个结论。假设 a 既不是左半部分的众数，也不是右半部分的众数，那么 a 出现的次数少于 l / 2 + r / 2 次，其中 l 和 r 分别是左半部分和右半部分的长度。由于 l / 2 + r / 2 <= (l + r) / 2，说明 a 也不是数组 nums 的众数，因此出现了矛盾。所以这个结论是正确的。

  这样以来，我们就可以使用分治法解决这个问题：将数组分成左右两部分，分别求出左半部分的众数 a1 以及右半部分的众数 a2，随后在 a1 和 a2 中选出正确的众数。

  算法

  我们使用经典的分治算法递归求解，直到所有的子问题都是长度为 1 的数组。长度为 1 的子数组中唯一的数显然是众数，直接返回即可。
  如果回溯后某区间的长度大于 1，我们必须将左右子区间的值合并。如果它们的众数相同，那么显然这一段区间的众数是它们相同的值。
  否则，我们需要比较两个众数在整个区间内出现的次数来决定该区间的众数。

"""


def majorityElement(nums):
    def findMajorityEl(low, high):
        # 只有一个元素 肯定为该集合的众数
        if low == high:
            return nums[low]
        # //运算符向下整除
        mid = (low + high) // 2
        # 处理左子表, 找到左子表的众数
        left = findMajorityEl(low, mid)
        # 处理右子表, 找到右子表的众数
        right = findMajorityEl(mid + 1, high)

        # 左右子表的众数相同
        if left == right:
            return left

        # 左右子表的众数不相同，统计[low, high]之间的众数
        left_count = 0
        right_count = 0
        for i in range(low, high + 1):
            if nums[i] == left:
                left_count += 1
            if nums[i] == right:
                right_count += 1

        return left if left_count > right_count else right

    return findMajorityEl(0, len(nums) - 1)


n = input()
nums = [int(num) for num in input().split()]
print(majorityElement(nums))
