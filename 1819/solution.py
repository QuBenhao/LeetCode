import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countDifferentSubsequenceGCDs(list(test_input))

    def countDifferentSubsequenceGCDs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 一个数x作为一个序列的最大公约数的必要条件是，序列中所有数都是x的倍数
        ans = 0
        nums = set(nums)
        c = max(nums)
        # 子序列的最大公约数只可能在1到最大值之间
        for i in range(1, c+1):
            g = None
            # 判断能否构造这个序列, 从i开始步长为i
            for j in range(i, c+1, i):
                # j 在nums中，尝试构造
                if j in nums:
                    if not g:
                        g = j
                    else:
                        g = math.gcd(j, g)
                    # 存在至少两个nums中的数，他们的最大公约数为i
                    if g == i:
                        ans += 1
                        break
        return ans
