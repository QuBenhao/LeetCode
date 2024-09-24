import solution
from typing import *
from collections import Counter, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minWindow(*test_input)

    def minWindow(self, s: str, t: str) -> str:
        ans_left, ans_right = -1, -1
        left, right = 0, 0
        t_count = Counter(t)
        diff = len(t_count)
        n = len(s)
        while right < n:
            if s[right] in t_count:
                t_count[s[right]] -= 1
                if t_count[s[right]] == 0:
                    diff -= 1
            while diff == 0:
                if ans_left == -1 or right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                if s[left] in t_count:
                    t_count[s[left]] += 1
                    if t_count[s[left]] == 1:
                        diff += 1
                left += 1
            right += 1
        return s[ans_left:ans_right + 1] if ans_left != -1 else ""
