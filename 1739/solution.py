import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumBoxes(test_input)

    def minimumBoxes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        z = 0
        q = 0
        while z < n:
            q += 1
            ans += q
            z += ans
        while z >= n + q:
            z -= q
            q -= 1
            ans -= 1
        return ans
