import solution
from itertools import permutations, combinations


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        return self.minimumIncompatibility(nums, k)

    def minimumIncompatibility(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == n:
            return 0
        dp = [[float("inf")] * n for _ in range(1 << n)]
        nums.sort()
        for i in range(n):
            dp[1 << i][i] = 0

        for mask in range(1 << n):
            n_z_bits = [len(bin(mask)) - p - 1 for p, c in enumerate(bin(mask)) if c == "1"]
            if len(n_z_bits) % (n // k) == 1:
                for j, l in permutations(n_z_bits, 2):
                    dp[mask][l] = min(dp[mask][l], dp[mask ^ (1 << l)][j])
            else:
                for j, l in combinations(n_z_bits, 2):
                    if nums[j] != nums[l]:
                        dp[mask][l] = min(dp[mask][l], dp[mask ^ (1 << l)][j] + nums[j] - nums[l])

        return min(dp[-1]) if min(dp[-1]) != float("inf") else -1
