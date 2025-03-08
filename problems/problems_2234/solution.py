import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumBeauty(*test_input)

    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        for i in range(n):
            flowers[i] = min(flowers[i], target)

        # 如果全部种满，还剩下多少朵花？
        left_flowers = newFlowers - (target * n - sum(flowers))

        # 没有种花，所有花园都已种满
        if left_flowers == newFlowers:
            return n * full  # 答案只能是 n*full（注意不能减少花的数量）

        # 可以全部种满
        if left_flowers >= 0:
            # 两种策略取最大值：留一个花园种 target-1 朵花，其余种满；或者，全部种满
            return max((target - 1) * partial + (n - 1) * full, n * full)

        flowers.sort()  # 时间复杂度的瓶颈在这，尽量写在后面

        ans = pre_sum = j = 0
        # 枚举 i，表示后缀 [i, n-1] 种满（i=0 的情况上面已讨论）
        for i in range(1, n + 1):
            # 撤销，flowers[i-1] 不变成 target
            left_flowers += target - flowers[i - 1]
            if left_flowers < 0:  # 花不能为负数，需要继续撤销
                continue

            # 满足以下条件说明 [0, j] 都可以种 flowers[j] 朵花
            while j < i and flowers[j] * j <= pre_sum + left_flowers:
                pre_sum += flowers[j]
                j += 1

            # 计算总美丽值
            # 在前缀 [0, j-1] 中均匀种花，这样最小值最大
            avg = (left_flowers + pre_sum) // j  # 由于上面特判了，这里 avg 一定小于 target
            total_beauty = avg * partial + (n - i) * full
            ans = max(ans, total_beauty)

        return ans
