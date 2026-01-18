from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.alternatingXOR(*test_input)

    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        counts1 = defaultdict(int) # 以target1结尾, 值为x的方案数
        counts2 = defaultdict(int) # 以target2结尾, 值为x的方案数
        counts2[0] = 1

        ans = 0
        pre = 0
        for num in nums:
            pre ^= num
            # target2后面拼一个target1的方案数, 即counts2[pre ^ target1]
            # target1后面拼一个target2的方案数, 即counts1[pre ^ target2]
            ans = (counts2[target1 ^ pre] + counts1[target2 ^ pre]) % MOD
            # 更新以target1结尾, 值为pre的方案数: 叠加counts2[pre ^ target1]
            # 更新以target2结尾, 值为pre的方案数: 叠加counts1[pre ^ target2]
            counts1[pre], counts2[pre] = (counts1[pre] + counts2[pre ^ target1]) % MOD, (counts2[pre] + counts1[pre ^ target2]) % MOD
        return ans

MOD = int(1e9) + 7
