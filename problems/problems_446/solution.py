import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfArithmeticSlices(list(test_input))

    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 分析，每三个数构成一个等差序列，那么从第一个数出发，和第二个数的差，要找到后面有没有等于第二个数加这个差的
        # 比如[2, 4, 6, 6, 6]中，2,4分别和3个6均可以构成一个答案
        # 固定前面的部分，我们要知道我们要找的val，以及val对应的前面的等差序列个数

        n, ans = len(nums), 0
        dp = [Counter() for _ in range(n)]
        # 目前某等差数列的末尾值(也有可能是只有它自己)
        for i in range(n - 1):
            # 加入这个值，能和这个末尾值的哪个等差序列构成等差序列吗？
            for j in range(i + 1, n):
                # 当前的差，用来比对和i构成的等差数列
                diff = nums[j] - nums[i]
                # 如果前面这个末尾有以diff为差的等差序列，那么j可以成为新的末尾，个数是它的个数加1, 多了个[i,j]等差序列！
                # 如果前面这个末尾没有以diff为差的等差序列，那么j和i构成一个等差序列的起始两位，个数为(0+1), 后面有和j差为diff的话，就可以构成等差序列了
                dp[j][diff] += dp[i][diff] + 1
                # i, j以及i前面的以diff为公差的等差序列，可以构成这么多新的等差序列
                # 这里和昨天的题一致, [i] 和 [j] 能构成等差序列只有当 [i] 有以 diff 为差的等差序列时 (至少两个数，因为加上j至少三个)
                ans += dp[i][diff]
        return ans
