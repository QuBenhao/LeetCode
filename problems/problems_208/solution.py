from typing import Optional

import solution
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Trie()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True

    def _search_node(self, word: str) -> Optional[dict]:
        node = self.root
        for c in word:
            if c not in node:
                return None
            node = node[c]
        return node

    def search(self, word: str) -> bool:
        return node.get("#", False) if (node := self._search_node(word)) else False

    def startsWith(self, prefix: str) -> bool:
        return self._search_node(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
