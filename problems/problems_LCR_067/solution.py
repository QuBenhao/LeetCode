import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMaximumXOR(test_input)

    def findMaximumXOR(self, nums: List[int]) -> int:
        root = {}

        def insert(word):
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word

        def search(word) -> Optional[str]:
            node = root
            for char in word:
                c = '1' if char == '0' else '0'
                if c in node:
                    node = node[c]
                    continue
                if char not in node:
                    return None
                node = node[char]
            return node.get('#', None)

        ans = 0
        b = len(bin(max(nums))) - 2
        for num in nums:
            wd = bin(num)[2:].zfill(b)
            if mx := search(wd):
                ans = max(ans, int(mx, 2) ^ num)
            insert(wd)

        return ans
