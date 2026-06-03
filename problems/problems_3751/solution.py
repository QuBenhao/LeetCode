from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.totalWaviness(*test_input)

    def totalWaviness(self, num1: int, num2: int) -> int:
        # 数位 DP：计算 [num1, num2] 范围内所有数字的波动值之和
        # 使用差分法：f(num2) - f(num1 - 1)

        def calc(n: int) -> int:
            """计算 [1, n] 范围内所有数字的波动值之和"""
            if n <= 0:
                return 0
            s = list(map(int, str(n)))

            @cache
            def dfs(i: int, prev: int, pre_prev: int, cnt: int,
                    limit: bool, is_num: bool) -> int:
                """
                i: 当前位
                prev: 前一个有效数位（-1 表示未开始）
                pre_prev: 前前一个有效数位（-1 表示不存在）
                cnt: 累计波动值
                limit: 是否受上界约束
                is_num: 是否已开始填数字
                """
                if i == len(s):
                    return cnt

                res = 0
                hi = s[i] if limit else 9

                # 不填数字（跳过/前导零）
                if not is_num:
                    res += dfs(i + 1, -1, -1, 0, False, False)

                # 填数字
                start = 1 if not is_num else 0
                for d in range(start, hi + 1):
                    new_cnt = cnt
                    # 判断 prev 是否是峰/谷
                    if prev != -1 and pre_prev != -1:
                        if pre_prev < prev > d:  # 峰
                            new_cnt += 1
                        elif pre_prev > prev < d:  # 谷
                            new_cnt += 1

                    res += dfs(i + 1, d, prev, new_cnt, limit and d == hi, True)

                return res

            return dfs(0, -1, -1, 0, True, False)

        return calc(num2) - calc(num1 - 1)
