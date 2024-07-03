import solution
from typing import *
from itertools import accumulate
from math import inf

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumMoves(*test_input)

    def minimumMoves(self, nums: List[int], k: int, max_changes: int) -> int:
        pos = []
        c = 0  # nums 中连续的 1 长度
        for i, x in enumerate(nums):
            if x == 0:
                continue
            pos.append(i)  # 记录 1 的位置
            c = max(c, 1)
            if i > 0 and nums[i - 1] == 1:
                if i > 1 and nums[i - 2] == 1:
                    c = 3  # 有 3 个连续的 1
                else:
                    c = max(c, 2)  # 有 2 个连续的 1

        c = min(c, k)
        if max_changes >= k - c:
            # 其余 k-c 个 1 可以全部用两次操作得到
            return max(c - 1, 0) + (k - c) * 2

        n = len(pos)
        pre_sum = list(accumulate(pos, initial=0))

        ans = inf
        # 除了 max_changes 个数可以用两次操作得到，其余的 1 只能一步步移动到 pos[i]
        size = k - max_changes
        for right in range(size, n + 1):
            # s1+s2 是 j 在 [left, right) 中的所有 pos[j] 到 pos[(left+right)/2] 的距离之和
            left = right - size
            i = left + size // 2
            s1 = pos[i] * (i - left) - (pre_sum[i] - pre_sum[left])
            s2 = pre_sum[right] - pre_sum[i] - pos[i] * (right - i)
            ans = min(ans, s1 + s2)
        return ans + max_changes * 2
