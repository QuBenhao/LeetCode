import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reinitializePermutation(test_input)

    def reinitializePermutation(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        mid = n // 2
        track = 1
        while track != mid:
            if track * 2 < n:
                track *= 2
            else:
                track = track * 2 + 1 - n
            ans += 1
        return ans
