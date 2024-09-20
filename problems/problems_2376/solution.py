import solution
from typing import *
from functools import cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSpecialNumbers(test_input)

    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return 1 if is_num else 0  # is_num 为 True 表示得到了一个合法数字
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = dfs(i + 1, mask, False, False)
            # 如果前面没有填数字，则必须从 1 开始（因为不能有前导零）
            low = 0 if is_num else 1
            # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            up = int(s[i]) if is_limit else 9
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if mask >> d & 1 == 0:  # d 不在 mask 中，说明之前没有填过 d
                    res += dfs(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res
        return dfs(0, 0, True, False)


