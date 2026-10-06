import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumBeauty(*test_input)

    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        for i in range(n):
            flowers[i] = min(flowers[i], target)

        # How many flowers remain if every garden is made complete?
        left_flowers = newFlowers - (target * n - sum(flowers))

        # Every garden is already complete before planting
        if left_flowers == newFlowers:
            return n * full  # The answer must be n*full (the number of flowers cannot be reduced)

        # Every garden can be made complete
        if left_flowers >= 0:
            # Take the better of two strategies: leave one garden with target-1 flowers and complete the others, or complete every garden
            return max((target - 1) * partial + (n - 1) * full, n * full)

        flowers.sort()  # This is the time-complexity bottleneck; defer it until after the early cases

        ans = pre_sum = j = 0
        # Enumerate i, making the suffix [i, n-1] complete (i=0 was handled above)
        for i in range(1, n + 1):
            # Undo the completion of flowers[i-1] to target
            left_flowers += target - flowers[i - 1]
            if left_flowers < 0:  # The remaining flower count cannot be negative; keep undoing
                continue

            # The following condition means every garden in [0, j] can have flowers[j] flowers
            while j < i and flowers[j] * j <= pre_sum + left_flowers:
                pre_sum += flowers[j]
                j += 1

            # Compute the total beauty
            # Distribute flowers evenly across [0, j-1] to maximize its minimum
            avg = (left_flowers + pre_sum) // j  # The special cases above guarantee avg is less than target here
            total_beauty = avg * partial + (n - i) * full
            ans = max(ans, total_beauty)

        return ans
