from collections import defaultdict
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, word1: str, word2: str) -> int:
        def update(counter, x, y):
            if x == y:
                return
            if counter[(y, x)] > 0:
                counter[(y, x)] -= 1
                # 因为刚刚有取到逆对, 所以用交换操作代替原来的替换操作, 操作数不需要变化了
            else:
                counter[(x, y)] += 1
                nonlocal op
                op += 1 # 暂时使用替换操作

        n = len(word1)

        # 预处理所有反转操作子串
        rev_op = [[0] * n for _ in range(n)]
        # 中心扩展法
        for i in range(2 * n - 1):
            cnt = defaultdict(int)
            op = 1 # 反转操作
            l, r = i // 2, (i+1) // 2
            while l >= 0 and r < n:
                update(cnt, word1[l], word2[r])
                if l != r:
                    update(cnt, word1[r], word2[l])
                rev_op[l][r] = op
                l -= 1
                r += 1

        f = [0] * (n + 1)
        for i in range(n):
            res = inf
            cnt = defaultdict(int)
            op = 0 # 正序不操作
            for j in range(i, -1, -1):
                update(cnt, word1[j], word2[j])
                res = min(res, f[j] + min(op, rev_op[j][i])) # 子串[j, i]的最小操作数
            f[i + 1] = res
        return f[n]
