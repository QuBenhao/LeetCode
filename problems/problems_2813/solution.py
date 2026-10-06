import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximumElegance(*test_input)

    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda p: -p[0])  # Sort profits in descending order
        ans = total_profit = 0
        vis = set()
        duplicate = []  # Profits from duplicate categories
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit  # Sum the profits of the first k items
                if category not in vis:
                    vis.add(category)
                else:  # Duplicate category
                    duplicate.append(profit)
            elif duplicate and category not in vis:  # A previously unseen category
                vis.add(category)  # len(vis) increases
                total_profit += profit - duplicate.pop()  # Replace the item with the smallest profit
            # else: lower profit and a duplicate category; choosing it only decreases total_profit while len(vis) stays unchanged, so elegance cannot increase
            ans = max(ans, total_profit + len(vis) * len(vis))
        return ans
