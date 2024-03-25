import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Trie()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class Trie:

    def __init__(self):
        pass


    def insert(self, word: str) -> None:
            pass


    def countWordsEqualTo(self, word: str) -> int:
            pass


    def countWordsStartingWith(self, prefix: str) -> int:
            pass


    def erase(self, word: str) -> None:
            pass



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)