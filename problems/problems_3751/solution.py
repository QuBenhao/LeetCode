from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalWaviness(*test_input)

    # 计算 [1, n] 中的整数的波动值之和
    def calc(self, n: int) -> int:
        ans = 0

        # 把整数划分成五段：prefix | l | m | r | suffix
        # 从低到高枚举 (l, m, r) 的位置，计算 (l, m, r) 对答案的贡献
        pow10 = 1
        while n >= pow10 * 100:
            max_prefix = n // (pow10 * 1000)
            n2 = n // pow10
            L = n2 // 100 % 10
            M = n2 // 10 % 10
            R = n2 % 10

            # 1. prefix < max_prefix 时，低位不受约束
            # 但 prefix=0 且 l=0 的情况是不合法的，需要减掉
            cnt = max_prefix * 570 - 45  # 先不与 pow10 相乘

            # 2. prefix = max_prefix 且 l < L
            cnt += (121 + L * 15 - L * L) * L // 3

            # 3. prefix = max_prefix 且 l = L 且 m < M
            cnt += (L + M) * max(M - L - 1, 0) // 2  # 峰
            cnt += (19 - min(L, M)) * min(L, M) // 2  # 谷

            # 4. prefix = max_prefix 且 l = L 且 m = M 且 r < R
            if L < M:  # 只能是峰
                cnt += min(M, R)
            elif L > M:  # 只能是谷
                cnt += max(R - M - 1, 0)

            # 到此为止，suffix 可以随便填，有 pow10 种填法
            ans += cnt * pow10

            # 5. prefix = max_prefix 且 l = L 且 m = M 且 r = R
            if (L - M) * (M - R) < 0:  # 峰或谷
                max_suffix = n % pow10
                ans += max_suffix + 1  # suffix 可以填 [0, max_suffix] 中的任意整数

            pow10 *= 10

        return ans

    def totalWaviness(self, num1: int, num2: int) -> int:
        return self.calc(num2) - self.calc(num1 - 1)

    # def totalWaviness(self, num1: int, num2: int) -> int:
    #     # 数位 DP：计算 [num1, num2] 范围内所有数字的波动值之和
    #     # 使用差分法：f(num2) - f(num1 - 1)
    #
    #     def calc(n: int) -> int:
    #         """计算 [1, n] 范围内所有数字的波动值之和"""
    #         if n <= 0:
    #             return 0
    #         s = list(map(int, str(n)))
    #
    #         @cache
    #         def dfs(i: int, prev: int, pre_prev: int, cnt: int,
    #                 limit: bool, is_num: bool) -> int:
    #             """
    #             i: 当前位
    #             prev: 前一个有效数位（-1 表示未开始）
    #             pre_prev: 前前一个有效数位（-1 表示不存在）
    #             cnt: 累计波动值
    #             limit: 是否受上界约束
    #             is_num: 是否已开始填数字
    #             """
    #             if i == len(s):
    #                 return cnt
    #
    #             res = 0
    #             hi = s[i] if limit else 9
    #
    #             # 不填数字（跳过/前导零）
    #             if not is_num:
    #                 res += dfs(i + 1, -1, -1, 0, False, False)
    #
    #             # 填数字
    #             start = 1 if not is_num else 0
    #             for d in range(start, hi + 1):
    #                 new_cnt = cnt
    #                 # 判断 prev 是否是峰/谷
    #                 if prev != -1 and pre_prev != -1:
    #                     if pre_prev < prev > d:  # 峰
    #                         new_cnt += 1
    #                     elif pre_prev > prev < d:  # 谷
    #                         new_cnt += 1
    #
    #                 res += dfs(i + 1, d, prev, new_cnt, limit and d == hi, True)
    #
    #             return res
    #
    #         return dfs(0, -1, -1, 0, True, False)
    #
    #     return calc(num2) - calc(num1 - 1)
