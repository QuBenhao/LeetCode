from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stringIndices(*test_input)

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        ord_a = ord('a')
        root = Node()
        for i, s in enumerate(wordsContainer):
            len_s = len(s)
            if len_s < root.min_len:
                root.min_len = len_s
                root.best_index = i

            # Insert s[::-1] into the trie
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ord_a
                if cur.son[c] is None:
                    cur.son[c] = Node()
                cur = cur.son[c]
                # Track the length and index of the shortest string in the subtree rooted at cur
                # Since i is visited in ascending order, do not update best_index when string lengths are equal
                if len_s < cur.min_len:
                    cur.min_len = len_s
                    cur.best_index = i

        ans = []
        for s in wordsQuery:
            cur = root
            for ch in reversed(s):
                c = ord(ch) - ord_a
                if cur.son[c] is None:
                    break
                cur = cur.son[c]
            # On loop exit, cur is the node for the longest common prefix; cur.best_index is the index of the shortest string with prefix cur
            ans.append(cur.best_index)
        return ans

class Node:
    __slots__ = 'son', 'min_len', 'best_index'

    def __init__(self):
        self.son = [None] * 26
        self.min_len = inf  # Length of the shortest string in the subtree
