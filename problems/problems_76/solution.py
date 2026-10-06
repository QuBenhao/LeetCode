import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minWindow(*test_input)

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        ans_left, ans_right = -1, len(s)
        left = 0
        cnt_s = Counter()  # Character counts in the substring of s
        cnt_t = Counter(t)  # Character counts in t
        less = len(cnt_t)  # less counts the character types whose frequencies are below those in t
        for right, c in enumerate(s):  # Move the substring's right endpoint
            cnt_s[c] += 1  # Add the character at the right endpoint to the substring
            if cnt_s[c] == cnt_t[c]:
                less -= 1  # The count of c changes from < to >= the required count
            while less == 0:  # Covered: every character count is >= the required count
                if right - left < ans_right - ans_left:  # Found a shorter substring
                    ans_left, ans_right = left, right  # Record the current left and right endpoints
                x = s[left]  # Character at the left endpoint
                if cnt_s[x] == cnt_t[x]:
                    less += 1  # The count of x changes from >= to < the required count after the next line runs
                cnt_s[x] -= 1  # Remove the character at the left endpoint from the substring
                left += 1  # Move the substring's left endpoint
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
