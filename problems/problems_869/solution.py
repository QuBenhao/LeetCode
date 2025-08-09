from collections import Counter
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reorderedPowerOf2(test_input)

    def reorderedPowerOf2(self, n: int) -> bool:
        return any(cur == pc for pc in POWERS) if (cur := Counter(str(n))) else False

MAX_N = int(1e9)
POWERS = [Counter(str(1 << i)) for i in range(31)]  # 2^0 to 2^30
