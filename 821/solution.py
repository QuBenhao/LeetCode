import solution


class Solution(solution.Solution):
    def solve(self, test_input):
        s, c = test_input
        return self.shortestToChar(str(s), str(c))

    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n = len(s)
        ans = [n] * n
        last = -1
        for i in range(n):
            if s[i] == c:
                if last >= 0:
                    last = (i + last) // 2
                for j in range(i - 1, last, -1):
                    ans[j] = min(i - j, ans[j])
                ans[i] = 0
                last = i
            elif last >= 0:
                ans[i] = min(i - last, ans[i])
        return ans
