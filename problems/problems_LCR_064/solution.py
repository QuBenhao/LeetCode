import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MagicDictionary()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = word

    @staticmethod
    def query(node, word, i, change):
        if i == len(word):
            return '#' in node and change
        if not change:
            for char in node:
                if char != '#' and MagicDictionary.query(node[char], word, i + 1, char != word[i]):
                    return True
            return False
        return word[i] in node and MagicDictionary.query(node[word[i]], word, i + 1, change)

    def search(self, searchWord: str) -> bool:
        return MagicDictionary.query(self.root, searchWord, 0, False)
