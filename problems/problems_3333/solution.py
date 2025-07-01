from itertools import accumulate

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.possibleStringCount(*test_input)

    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        idx = 0
        ans = 1
        word += " "
        groups = []
        while idx < n:
            start = idx
            while idx < n and word[idx] == word[idx + 1]:
                idx += 1
            length = idx - start + 1
            if length > 1:
                groups.append(length - 1)
            k -= 1
            ans = ans * length % MOD
            idx += 1
        if k <= 0:
            return ans
        # less than k
        f = [[0] * k for _ in range(len(groups) + 1)]
        f[0] = [1] * k
        for i, c in enumerate(groups):
            # 计算 f[i] 的前缀和数组 s
            s = list(accumulate(f[i], initial=0))
            # 计算子数组和
            for j in range(k):
                f[i + 1][j] = (s[j + 1] - s[max(j - c, 0)]) % MOD

        return (ans - f[-1][-1]) % MOD


MOD = 10 ** 9 + 7
