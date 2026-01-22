from collections import defaultdict
from heapq import heapify, heappop, heappush
from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumPairRemoval(test_input)

    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        h = []  # (相邻元素和，左边那个数的下标)
        dec = 0  # 递减的相邻对的个数
        for i, (x, y) in enumerate(pairwise(nums)):
            if x > y:
                dec += 1
            h.append((x + y, i))
        heapify(h)
        lazy = defaultdict(int)

        # 每个下标的左右最近的未删除下标
        left = list(range(-1, n))  # 加一个哨兵，防止下标越界
        right = list(range(1, n + 1))

        ans = 0
        while dec:
            ans += 1

            while lazy[h[0]]:
                lazy[heappop(h)] -= 1
            s, i = heappop(h)  # 删除相邻元素和最小的一对

            # (当前元素，下一个数)
            nxt = right[i]
            if nums[i] > nums[nxt]:  # 旧数据
                dec -= 1

            # (前一个数，当前元素)
            pre = left[i]
            if pre >= 0:
                if nums[pre] > nums[i]:  # 旧数据
                    dec -= 1
                if nums[pre] > s:  # 新数据
                    dec += 1
                lazy[(nums[pre] + nums[i], pre)] += 1  # 懒删除
                heappush(h, (nums[pre] + s, pre))

            # (下一个数，下下一个数)
            nxt2 = right[nxt]
            if nxt2 < n:
                if nums[nxt] > nums[nxt2]:  # 旧数据
                    dec -= 1
                if s > nums[nxt2]:  # 新数据（当前元素，下下一个数）
                    dec += 1
                lazy[(nums[nxt] + nums[nxt2], nxt)] += 1  # 懒删除
                heappush(h, (s + nums[nxt2], i))

            nums[i] = s
            # 删除 nxt
            l, r = left[nxt], right[nxt]
            right[l] = r  # 模拟双向链表的删除操作
            left[r] = l

        return ans
