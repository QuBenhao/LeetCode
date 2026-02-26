import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSteps(test_input)

    def numSteps(self, s: str) -> int:
        # carry = 0
        # ans = len(s) - 1 # 除第一位以外每位1或0都至少操作一次
        # for i in range(len(s) - 1, 0, -1):
        #     cur = carry + int(s[i])
        #     ans += 1 if cur == 1 else 0 # 奇数需要额外+1
        #     carry = 0 if cur == 0 else 1 # 产生进位
        # return ans + carry

        # 从上面的规律可以发现, 最右侧1左边的0才会有额外的奇数贡献
        ans = len(s) - 1
        if (idx := s.rfind('1')) > 0:
            # 存在最右侧1左边的0, 每个0需要额外+1, 且idx处和0处各需要+1
            ans += s.count('0', 1, idx) + 2
        return ans
