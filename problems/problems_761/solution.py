import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.makeLargestSpecial(test_input)

    def makeLargestSpecial(self, s: str) -> str:
        # cur: 前缀和统计, last: 上一个特殊序列的结尾
        cur = last = 0
        # 所有可选的子特殊序列
        candidates = []
        for i, c in enumerate(s):
            cur += 1 if c == '1' else -1
            # 出现特殊序列, 一定是以1开头以0结尾
            if not cur:
                # 先将当前特殊序列排成最大, 首尾最终仍是1和0不可动，所以递归去掉头尾
                candidates.append('1' + self.makeLargestSpecial(s[last + 1:i]) + '0')
                last = i + 1
        # 所有特殊子序列可以无限次交换，因此从大到小依次排列拼接即可
        return "".join(sorted(candidates, reverse=True))
