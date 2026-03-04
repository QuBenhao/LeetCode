import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(str(test_input))

    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        a1 = a2 = 0
        for i in range(n):
            if i & 1 == ord(s[i]) & 1:
                a1 += 1
            else:
                a2 += 1
        return min(a1,a2)
