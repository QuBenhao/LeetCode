import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Trie()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        pass

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        pass

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pass

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pass

