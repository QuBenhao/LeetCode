import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestAltitude(list(test_input))

    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans = curr = 0
        for g in gain:
            curr += g
            if curr > ans:
                ans = curr
        return ans
