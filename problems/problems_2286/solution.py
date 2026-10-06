import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = BookMyShow(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.min = [0] * (2 << n.bit_length())  # Uses less space than 4n
        self.sum = [0] * (2 << n.bit_length())

    # Segment tree: increase the element at index i by val
    def update(self, o: int, l: int, r: int, i: int, val: int) -> None:
        if l == r:
            self.min[o] += val
            self.sum[o] += val
            return
        m = (l + r) // 2
        if i <= m:
            self.update(o * 2, l, m, i, val)
        else:
            self.update(o * 2 + 1, m + 1, r, i, val)
        self.min[o] = min(self.min[o * 2], self.min[o * 2 + 1])
        self.sum[o] = self.sum[o * 2] + self.sum[o * 2 + 1]

    # Segment tree: return the sum of elements in [L,R]
    def query_sum(self, o: int, l: int, r: int, L: int, R: int) -> int:
        if L <= l and r <= R:
            return self.sum[o]
        res = 0
        m = (l + r) // 2
        if L <= m:
            res = self.query_sum(o * 2, l, m, L, R)
        if R > m:
            res += self.query_sum(o * 2 + 1, m + 1, r, L, R)
        return res

    # Segment tree: return the leftmost position in [0,R] whose value is <= val, or -1 if none exists
    def find_first(self, o: int, l: int, r: int, R: int, val: int) -> int:
        if self.min[o] > val:
            return -1  # Every value in the interval exceeds val
        if l == r:
            return l
        m = (l + r) // 2
        if self.min[o * 2] <= val:
            return self.find_first(o * 2, l, m, R, val)
        if R > m:
            return self.find_first(o * 2 + 1, m + 1, r, R, val)
        return -1

    def gather(self, k: int, maxRow: int) -> List[int]:
        # Find the first bucket that can hold k more liters of water
        r = self.find_first(1, 0, self.n - 1, maxRow, self.m - k)
        if r < 0:  # No such bucket exists
            return []
        c = self.query_sum(1, 0, self.n - 1, r, r)
        self.update(1, 0, self.n - 1, r, k)  # Pour water
        return [r, c]

    def scatter(self, k: int, maxRow: int) -> bool:
        # Total amount of water in [0,maxRow]
        s = self.query_sum(1, 0, self.n - 1, 0, maxRow)
        if s > self.m * (maxRow + 1) - k:
            return False  # The buckets already contain too much water
        # Start with the first bucket that is not full
        i = self.find_first(1, 0, self.n - 1, maxRow, self.m - 1)
        while k:
            left = min(self.m - self.query_sum(1, 0, self.n - 1, i, i), k)
            self.update(1, 0, self.n - 1, i, left)  # Pour water
            k -= left
            i += 1
        return True
