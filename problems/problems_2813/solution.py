import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximumElegance(*test_input)

    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda p: -p[0])  # 把利润从大到小排序
        ans = total_profit = 0
        vis = set()
        duplicate = []  # 重复类别的利润
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit  # 累加前 k 个项目的利润
                if category not in vis:
                    vis.add(category)
                else:  # 重复类别
                    duplicate.append(profit)
            elif duplicate and category not in vis:  # 之前没有的类别
                vis.add(category)  # len(vis) 变大
                total_profit += profit - duplicate.pop()  # 用最小利润替换
            # else: 比前面的利润小，而且类别还重复了，选它只会让 total_profit 变小，len(vis) 不变，优雅度不会变大
            ans = max(ans, total_profit + len(vis) * len(vis))
        return ans
