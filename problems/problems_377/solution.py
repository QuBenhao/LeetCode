import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        return self.combinationSum4(list(nums), target)

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # from functools import lru_cache
        # @lru_cache(None)
        # def bfs(remain):
        #     if remain == 0:
        #         return 1
        #     ans = 0
        #     for num in nums:
        #         if num > remain:
        #             break
        #         ans += bfs(remain-num)
        #     return ans
        #
        # nums.sort()
        # return bfs(target)

        nums.sort()
        # dp[i]: 组合成i的组合数
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num > i:
                    break
                dp[i] += dp[i-num]
        return dp[-1]
