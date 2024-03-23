import solution
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canEat(*test_input)

    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # day + 1 是因为我们考虑的是需要的天数而不是第几天，第二天实际上已经吃第三天了
        # 按最快的速度 cap 吃，至少需要的天数（把前面的presum[ty]吃光）
        # presum[ty+1] 按最慢的速度吃，至多的天数
        presum = list(accumulate([0] + candiesCount))
        return [presum[t]//c <= d < presum[t+1] for t,d,c in queries]
