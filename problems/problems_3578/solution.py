from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPartitions(*test_input)

    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD =  10**9 + 7
        n = len(nums)
        min_q = deque() # 单调递增队列 维护窗口最小值
        max_q = deque() # 单调递减队列 维护窗口最大值
        f = [0] * (n+1) # f[i] 表示以 nums[i-1] 结尾的子数组的合法分割数
        f[0] = 1 # 初始状态，空数组有1种分割方式
        sum_f = 0 # 记录当前窗口内的合法分割数之和
        left = 0

        for i, x in enumerate(nums):
            sum_f += f[i] # 当前滑窗累计合法分割数

            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            while nums[max_q[0]] - nums[min_q[0]] > k: # 如果当前窗口的最大值和最小值之差超过 k, 必须移动坐端点
                sum_f -= f[left]
                left += 1
                if min_q[0] < left:
                    min_q.popleft()
                if max_q[0] < left:
                    max_q.popleft()

            f[i + 1] = sum_f % MOD

        return f[n] % MOD
