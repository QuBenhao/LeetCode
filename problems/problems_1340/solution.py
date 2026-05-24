import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxJumps(*test_input)

    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)

        # 单调栈预处理：每个位置左右两侧第一个 >= 自身高度的障碍位置
        # right[i] = i 右侧第一个 arr[j] >= arr[i] 的下标，不存在则为 n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                right[stack.pop()] = i
            stack.append(i)

        # left[i] = i 左侧第一个 arr[j] >= arr[i] 的下标，不存在则为 -1
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # DP：按高度从小到大处理
        indices = sorted(range(n), key=lambda i: arr[i])
        dp = [1] * n

        for i in indices:
            lo = max(left[i] + 1, i - d)
            hi = min(right[i] - 1, i + d)
            for j in range(lo, hi + 1):
                if j != i:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

