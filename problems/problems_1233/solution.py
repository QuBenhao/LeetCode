import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeSubfolders(test_input)

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = {}

        def insert(word):
            node = root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True

        def has_prefix(word):
            node = root
            for char in word:
                if '#' in node:
                    return True
                if char not in node:
                    return False
                node = node[char]
            return '#' in node

        ans = []
        for f in sorted(folder, key=lambda x: len(x)):
            w = f.split('/')[1:]
            if has_prefix(w):
                continue
            insert(w)
            ans.append(f)
        return ans
