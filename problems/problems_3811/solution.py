from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.alternatingXOR(*test_input)

    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        counts1 = defaultdict(int) # Number of ways ending with target1 and having value x
        counts2 = defaultdict(int) # Number of ways ending with target2 and having value x
        counts2[0] = 1

        ans = 0
        pre = 0
        for num in nums:
            pre ^= num
            # Number of ways to append target1 after target2, i.e. counts2[pre ^ target1]
            # Number of ways to append target2 after target1, i.e. counts1[pre ^ target2]
            ans = (counts2[target1 ^ pre] + counts1[target2 ^ pre]) % MOD
            # Update the number of ways ending with target1 and having value pre: add counts2[pre ^ target1]
            # Update the number of ways ending with target2 and having value pre: add counts1[pre ^ target2]
            counts1[pre], counts2[pre] = (counts1[pre] + counts2[pre ^ target1]) % MOD, (counts2[pre] + counts1[pre ^ target2]) % MOD
        return ans

MOD = int(1e9) + 7
