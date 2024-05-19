import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minWindow(*test_input)

    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        ans_left, ans_right = -1, len(s)
        left = 0
        cnt_s = Counter()  # s 子串字母的出现次数
        cnt_t = Counter(t)  # t 中字母的出现次数
        less = len(cnt_t)  # 有 less 种字母的出现次数 < t 中的字母出现次数
        for right, c in enumerate(s):  # 移动子串右端点
            cnt_s[c] += 1  # 右端点字母移入子串
            if cnt_s[c] == cnt_t[c]:
                less -= 1  # c 的出现次数从 < 变成 >=
            while less == 0:  # 涵盖：所有字母的出现次数都是 >=
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点
                x = s[left]  # 左端点字母
                if cnt_s[x] == cnt_t[x]:
                    less += 1  # x 的出现次数从 >= 变成 <（下一行代码执行后）
                cnt_s[x] -= 1  # 左端点字母移出子串
                left += 1  # 移动子串左端点
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]
