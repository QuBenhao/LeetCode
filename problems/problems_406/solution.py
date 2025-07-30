from typing import List

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reconstructQueue(test_input)

    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda p: (p[0], -p[1]))
        # 插入时，前面插入的对当前都没有影响，后面的都有影响，所以是第p[i][1]+1个空位置
        n = len(people)
        fw = FenwickTree(n)
        ans = [[] for _ in range(n)]
        for i in range(1, n + 1):
            l, r = 1, n
            while l < r:
                mid = (l + r) // 2
                # 查询前mid个位置中有多少人，应该至多剩下mid - people[i - 1][1]个空位
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
        self.tree = [0] * (self.n + 1)  # 索引从1开始

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int) -> None:
        """ 单点更新：a[idx] += delta """
        while idx <= self.n:
            self.tree[idx] += delta
            idx += self.lowbit(idx)

    def query(self, idx: int) -> int:
        """ 查询前缀和：a[1] + a[2] + ... + a[idx] """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

    def range_query(self, l: int, r: int) -> int:
        """ 区间查询：a[l] + a[l+1] + ... + a[r] """
        return self.query(r) - self.query(l - 1)
