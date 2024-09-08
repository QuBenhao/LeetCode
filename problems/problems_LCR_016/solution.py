from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lengthOfLongestSubstring(test_input)

    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        ans = 0
        window = deque()
        for i, c in enumerate(s):
            if c in record:
                while window and window[0] != c:
                    record.pop(window.popleft())
                window.popleft()
            window.append(c)
            record[c] = i
            ans = max(ans, len(window))
        return ans
