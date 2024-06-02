import solution
from typing import *
from math import ceil


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distributeCandies(*test_input)

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        x * (x + 1) // 2 >= candies > x * (x - 1) // 2
        (x + 1) * (x + 1) > x * (x + 1) >= 2 * candies > x * (x - 1) > (x - 1) * (x - 1)
        x + 1 > 根号下(2 * candies) > x - 1
        {} + 1 > x > {} - 1
        """
        f = (candies * 2) ** 0.5
        # 从最大往最小逼近
        x = int(f + 1)
        if (s := x * (x + 1) // 2) > candies:
            s -= x
            if s > candies:
                x -= 1
                s -= x
            x -= 1
        remain = candies - s
        d, m = divmod(x, num_people)
        ans = [0] * num_people
        for i in range(num_people):
            ans[i] = (i + 1) * d + num_people * (d - 1) * d // 2
            if i < m:
                ans[i] += i + 1 + num_people * d
        ans[m] += remain
        return ans
