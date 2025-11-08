import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPower(*test_input)

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # 滑动窗口
        s = sum(stations[:r])  # 先计算 [0, r-1] 的发电量，为第一个窗口做准备
        power = [0] * n
        for i in range(n):
            # 右边进
            if (right := i + r) < n:
                s += stations[right]
            # 左边出
            if (left := i - r - 1) >= 0:
                s -= stations[left]
            power[i] = s

        def check(low: int) -> bool:
            diff = [0] * n  # 差分数组
            sum_d = built = 0
            for i, p in enumerate(power):
                sum_d += diff[i]  # 累加差分值
                m = low - (p + sum_d)
                if m <= 0:
                    continue
                # 需要在 i+r 额外建造 m 个供电站
                built += m
                if built > k:  # 不满足要求
                    return False
                # 把区间 [i, i+2r] 加一
                sum_d += m  # 由于 diff[i] 后面不会再访问，我们直接加到 sum_d 中
                if (right := i + r * 2 + 1) < n:
                    diff[right] -= m
            return True

        # 开区间二分
        mn = min(power)
        left, right = mn + k // n, mn + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
