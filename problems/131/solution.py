import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.partition(test_input)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    if j == i - 1:
                        dp[j][i] = True
                    else:
                        dp[j][i] = dp[j + 1][i - 1]

        ans = []

        def dfs(index, curr):
            if index == n:
                ans.append(curr)
                return
            for i in range(index, n):
                if dp[index][i]:
                    temp = list(curr)
                    temp.append(s[index:i + 1])
                    dfs(i + 1, temp)

        dfs(0, [])
        return ans
