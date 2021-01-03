import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.waysToSplit(list(test_input))

    def waysToSplit(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        ans = j = k = 0
        for i in range(1, len(nums)):
            j = max(j, i + 1)
            while j < len(nums) and 2 * prefix[i] > prefix[j]:
                j += 1
            k = max(k, j)
            while k < len(nums) and 2 * prefix[k] <= prefix[i] + prefix[-1]:
                k += 1
            ans += k - j
        return ans % mod
