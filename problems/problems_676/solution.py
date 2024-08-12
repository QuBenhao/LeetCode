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
        self.root = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = True
    
    @staticmethod
    def query(node, word: str, remain: int) -> bool:
        if not word:
            return remain == 0 and (isinstance(node, bool) or node.get("#", False))
        nxt = word[1:]
        if word[0] in node:
            if MagicDictionary.query(node[word[0]], nxt, remain):
                return True
        if not remain:
            return False
        for c in node:
            if c == word[0] or c == "#":
                continue
            if MagicDictionary.query(node[c], nxt, remain - 1):
                return True
        return False

    def search(self, searchWord: str) -> bool:
        return MagicDictionary.query(self.root, searchWord, 1)
