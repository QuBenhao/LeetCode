from heapq import heappush, heappop
from itertools import combinations
from math import inf, floor

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minTime(*test_input)

    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        total_mask = 1 << n
        init_mask = total_mask - 1

        graph = [[] for _ in range(total_mask)]
        for i in range(total_mask):
            bits = [j for j in range(n) if (i >> j) & 1]
            for size in range(1, min(len(bits), k) + 1):
                for ng in combinations(bits, size):
                    graph[i].append((ng, max(time[idx] for idx in ng)))

        dp = [[[inf] * 2 for _ in range(m)] for _ in range(total_mask)]
        dp[init_mask][0][0] = 0
        # 0 for start side, 1 for opposite
        pq = [(0, init_mask, 0, 0)] # time, mask, m, side
        while pq:
            t, mask, cur_m, side = heappop(pq)
            if dp[mask][cur_m][side] < t:
                continue
            if side == 0:
                for ng, cost in graph[mask]:
                    new_mask = mask
                    for idx in ng:
                        new_mask ^= 1 << idx
                    time_cost = cost * mul[cur_m]
                    new_m = (cur_m + floor(time_cost)) % m
                    if dp[new_mask][new_m][1] > (new_t := t + time_cost):
                        dp[new_mask][new_m][1] = new_t
                        heappush(pq, (new_t, new_mask, new_m, 1))
            else:
                if mask == 0:
                    return t
                for i in range(n):
                    if ((mask >> i) & 1) == 0:
                        new_mask = mask ^ (1 << i)
                        time_cost = time[i] * mul[cur_m]
                        new_m = (cur_m + floor(time_cost)) % m
                        if dp[new_mask][new_m][0] > (new_t := t + time_cost):
                            dp[new_mask][new_m][0] = new_t
                            heappush(pq, (new_t, new_mask, new_m, 0))
        return -1.0
