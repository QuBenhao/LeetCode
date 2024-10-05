import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTime(*test_input)

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_t = min(time)
        avg = (totalTrips - 1) // len(time) + 1
        left = min_t * avg - 1  # 循环不变量：sum >= totalTrips 恒为 False
        right = min(max(time) * avg, min_t * totalTrips)  # 循环不变量：sum >= totalTrips 恒为 True
        while left + 1 < right:  # 开区间 (left, right) 不为空
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid  # 缩小二分区间为 (left, mid)
            else:
                left = mid  # 缩小二分区间为 (mid, right)
        # 此时 left 等于 right-1
        # sum(left) < totalTrips 且 sum(right) >= totalTrips，所以答案是 right
        return right
