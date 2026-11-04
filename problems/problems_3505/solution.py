import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}

        counts = Fenwick(len(values))
        sums = Fenwick(len(values))
        total = 0
        for v in nums[:x]:
            i = rank[v]
            counts.add(i, 1)
            sums.add(i, v)
            total += v

        # Cost of the current window: sum |v - med|, med = lower median.
        mid_rank = (x + 1) // 2

        def window_cost():
            idx = counts.kth(mid_rank)
            cnt_le = counts.prefix(idx)
            sum_le = sums.prefix(idx)
            med = values[idx - 1]
            return med * cnt_le - sum_le + (total - sum_le) - med * (x - cnt_le)

        cost = [0] * (n - x + 1)
        cost[0] = window_cost()
        for start in range(1, n - x + 1):
            out_v, in_v = nums[start - 1], nums[start + x - 1]
            out_i, in_i = rank[out_v], rank[in_v]
            counts.add(out_i, -1)
            sums.add(out_i, -out_v)
            counts.add(in_i, 1)
            sums.add(in_i, in_v)
            total += in_v - out_v
            cost[start] = window_cost()

        # dp: min cost of j non-overlapping length-x windows in the prefix.
        prev = [0] * (n + 1)
        for _ in range(k):
            cur = [10 ** 30] * (n + 1)
            for i in range(1, n + 1):
                best = cur[i - 1]
                if i >= x:
                    cand = prev[i - x] + cost[i - x]
                    if cand < best:
                        best = cand
                cur[i] = best
            prev = cur
        return prev[n]

class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.tree = [0] * (n + 1)

    def add(self, i: int, delta: int) -> None:
        tree, n = self.tree, self.n
        while i <= n:
            tree[i] += delta
            i += i & -i

    def prefix(self, i: int) -> int:
        s = 0
        tree = self.tree
        while i > 0:
            s += tree[i]
            i -= i & -i
        return s

    def kth(self, k: int) -> int:
        """Smallest 1-based index whose prefix count is at least k."""
        tree, n = self.tree, self.n
        pos = 0
        for pw in range(n.bit_length() - 1, -1, -1):
            nxt = pos + (1 << pw)
            if nxt <= n and tree[nxt] < k:
                pos = nxt
                k -= tree[nxt]
        return pos + 1
