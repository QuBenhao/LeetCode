import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestSubsequence(*test_input)

    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_left = s.count(letter)
        ans = []
        cur_letter = 0
        n = len(s)
        for i, c in enumerate(s):
            # 条件1: 单调递增栈, 保证字典序最小
            # 条件2: 保证长度为k (还剩n-i个数, 已经有len(ans)个数, 要去掉栈顶一个数, 整体长度仍能到k)
            # 条件3: 保证letter的个数至少为repetition
            while (ans and ans[-1] > c and n - i + len(ans) - 1 >= k and
                   (c == letter or letter_left + cur_letter - (ans[-1] == letter) >= repetition)):
                if ans.pop() == letter:
                    cur_letter -= 1
            if len(ans) < k:
                if c == letter:
                    cur_letter += 1
                    ans.append(c)
                elif k - len(ans) > repetition - cur_letter:
                    ans.append(c)
            if c == letter:
                letter_left -= 1
        return "".join(ans)
