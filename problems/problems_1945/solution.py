import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getLucky(*test_input)

    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans = 0
        for c in s:
            tmp = ord(c) - ord('a') + 1
            ans += tmp % 10 + tmp // 10
        for i in range(k-1):
            prev = ans
            ans = 0
            while prev:
                ans += prev % 10
                prev //= 10
        return ans
