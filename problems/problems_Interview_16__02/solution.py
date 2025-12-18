import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = WordsFrequency(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class WordsFrequency:
    def __init__(self, book: List[str]):
        pass

    def get(self, word: str) -> int:
        pass

