import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, maximumBit = test_input
        return self.getMaximumXor(list(nums), maximumBit)

    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        ans = [0] * n
        for i in range(n):
            res[i] = res[i-1] ^ nums[i]
        ans[0] = res[-1] ^ (2**maximumBit - 1)
        idx = n - 1
        for i in range(1,n):
            ans[i] = ans[i-1] ^ nums[idx]
            idx -= 1
        return ans
