import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestCycle(test_input)

    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        cur_time = 1  # 当前时间
        vis_time = [0] * n  # 首次访问 x 的时间
        for x in range(n):
            start_time = cur_time  # 本轮循环的开始时间
            while x != -1 and vis_time[x] == 0:  # 没有访问过 x
                vis_time[x] = cur_time  # 记录访问 x 的时间
                cur_time += 1
                x = edges[x]  # 访问下一个节点
            if x != -1 and vis_time[x] >= start_time:  # x 在本轮循环中访问了两次，说明 x 在环上
                ans = max(ans, cur_time - vis_time[x])  # 前后两次访问 x 的时间差，即为环长
        return ans  # 如果没有找到环，返回的是 ans 的初始值 -1
