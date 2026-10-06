from typing import List

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reconstructQueue(test_input)

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (p[0], -p[1]))
        # Earlier insertions do not affect the current person, while later ones do, so use the (p[i][1]+1)th empty position
        n = len(people)
        fw = FenwickTree(n)
        ans = [[] for _ in range(n)]
        for i in range(1, n + 1):
            l, r = 1, n
            while l < r:
                mid = (l + r) // 2
                # Query the number of people in the first mid positions; at most mid - people[i - 1][1] empty positions should remain
                if fw.query(mid) >= mid - people[i - 1][1]:
                    l = mid + 1
                else:
                    r = mid
            fw.update(l, 1)
            ans[l - 1] = people[i - 1]
        return ans


class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (self.n + 1)  # Indices start at 1

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int) -> None:
        """ Point update: a[idx] += delta """
        while idx <= self.n:
            self.tree[idx] += delta
            idx += self.lowbit(idx)

    def query(self, idx: int) -> int:
        """ Query the prefix sum: a[1] + a[2] + ... + a[idx] """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

    def range_query(self, l: int, r: int) -> int:
        """ Range query: a[l] + a[l+1] + ... + a[r] """
        return self.query(r) - self.query(l - 1)
