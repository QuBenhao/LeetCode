import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestCommonPrefix(*test_input)

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = {}

        # Insert the number into the Trie
        for num in arr1:
            node = root
            for c in str(num):
                if c not in node:
                    node[c] = {}
                node = node[c]

        # Walk the Trie once and record the depth reached
        def query(num: int) -> int:
            node = root
            s = str(num)
            depth = 0
            for c in s:
                if c not in node:
                    break
                node = node[c]
                depth += 1
            return depth

        return max((query(num) for num in arr2), default=0)

