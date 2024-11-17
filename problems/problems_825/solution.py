from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numFriendRequests(test_input)

    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1

        ans = cnt_window = age_y = 0
        for age_x, c in enumerate(cnt):
            cnt_window += c
            if age_y * 2 <= age_x + 14:  # 不能发送好友请求
                cnt_window -= cnt[age_y]
                age_y += 1
            if cnt_window:  # 存在可以发送好友请求的用户
                ans += c * cnt_window - c
        return ans
