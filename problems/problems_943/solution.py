import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestSuperstring(test_input)

    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        g = [[0] * n for _ in range(n)] # g[i][j] represents the overlap length of words[i] suf and words[j] pre
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(min(len(words[i]), len(words[j])), 0, -1):
                    if words[i][-k:] == words[j][:k]:
                        g[i][j] = k
                        break
        mask = 1 << n
        dp = [[0] * n for _ in range(mask)] # dp[mask][i] represents the max overlap length of words in mask ending with words[i]
        # the final answer should be sum(len(word) for word in words) - max(dp[mask-1])
        track = [[-1] * n for _ in range(mask)] # track[mask][i] represents the previous word index before words[i] in the optimal path for mask
        for s in range(1, mask):
            for i in range(n):
                if ((s >> i) & 1) == 0: # s 不可能以 words[i] 结尾
                    continue
                for j in range(n):
                    if ((s >> j) & 1) == 1: # s 已经包含 words[j]
                        continue
                    if dp[ns := s | (1 << j)][j] < dp[s][i] + g[i][j]:
                        dp[ns][j] = dp[s][i] + g[i][j]
                        track[ns][j] = i
        max_i = max(range(n), key=lambda x: dp[mask - 1][x])
        st = mask - 1
        ans = [words[max_i]]
        while st != 0:
            prev = max_i
            max_i, st = track[st][max_i], st ^ (1 << max_i)
            if max_i != -1:
                ans.append(words[max_i][:len(words[max_i]) - g[max_i][prev]])
            else:
                max_i = max([i for i in range(n) if (st >> i) & 1], key=lambda x: dp[st], default=-1)
                if max_i != -1:
                    ans.append(words[max_i])
        ans.reverse()
        return "".join(ans)
