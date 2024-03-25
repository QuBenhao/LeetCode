import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = PhoneDirectory(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        pass


    def get(self) -> int:
        pass


    def check(self, number: int) -> bool:
            pass


    def release(self, number: int) -> None:
            pass



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)