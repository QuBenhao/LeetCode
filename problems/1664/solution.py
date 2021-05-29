import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToMakeFair(list(test_input))

    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 偶数和与奇数和的差
        delta = sum(nums[0::2]) - sum(nums[1::2])
        # 符号
        flag = 1
        res = 0
        # 当前的和
        cur = 0
        for i, num in enumerate(nums):
            # 减去两倍前面的和可以使得符号颠倒（之前加的偶数和变为减，减的奇数和变为加）
            if delta - 2 * cur - flag * num == 0:
                res += 1
            cur += flag * num
            flag *= -1
        return res

