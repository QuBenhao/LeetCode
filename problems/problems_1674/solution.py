import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMoves(*test_input)

    def minMoves(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        n = len(nums)
        # The final pair sum must be in [2, 2 * limit]
        diff = [0] * (2 * limit + 2)
        # For each pair nums[i], nums[n-1-i]:
        # Only diff[a + b] requires no changes
        # One change suffices in [1 + min(a, b), limit + max(a, b) + 1)
        # The remaining sums require two changes
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            # Two changes required
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            # One change required
            diff[1 + min(a, b)] -= 1
            diff[limit + max(a, b) + 1] += 1
            # Zero changes required
            diff[a + b] -= 1
            diff[a + b + 1] += 1
        res, s = n, 0
        for i in range(2, 2 * limit + 1):
            s += diff[i]
            res = min(res, s)
        return res
