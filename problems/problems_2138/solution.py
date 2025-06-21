import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.divideString(*test_input)

    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:i + k] if i + k <= n else s[i:i + k] + fill * (i + k - n) for i in range(0, n, k)] if (n := len(s)) else []
