import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfUnplacedFruits(*test_input)

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        t = SegmentTree(baskets)
        n = len(baskets)
        ans = 0
        for x in fruits:
            if t.find_first_and_update(1, 0, n - 1, x) < 0:
                ans += 1
        return ans

class SegmentTree:
    def __init__(self, a: List[int]):
        n = len(a)
        self.max = [0] * (2 << (n - 1).bit_length())
        self.build(a, 1, 0, n - 1)

    def maintain(self, o: int):
        self.max[o] = max(self.max[o * 2], self.max[o * 2 + 1])

    # Initialize the segment tree
    def build(self, a: List[int], o: int, l: int, r: int):
        if l == r:
            self.max[o] = a[l]
            return
        m = (l + r) // 2
        self.build(a, o * 2, l, m)
        self.build(a, o * 2 + 1, m + 1, r)
        self.maintain(o)

    # Find the first number >= x in the interval, set it to -1, and return its index (or -1 if none exists)
    def find_first_and_update(self, o: int, l: int, r: int, x: int) -> int:
        if self.max[o] < x:  # No number in the interval is >= x
            return -1
        if l == r:
            self.max[o] = -1  # Set to -1 to indicate that fruit can no longer be placed here
            return l
        m = (l + r) // 2
        i = self.find_first_and_update(o * 2, l, m, x)  # Recurse into the left subtree first
        if i < 0:  # Not found in the left subtree
            i = self.find_first_and_update(o * 2 + 1, m + 1, r, x)  # Then recurse into the right subtree
        self.maintain(o)
        return i
