import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Excel(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class Excel:

    def __init__(self, height: int, width: str):
            pass


    def set(self, row: int, column: str, val: int) -> None:
                pass


    def get(self, row: int, column: str) -> int:
            pass


    def sum(self, row: int, column: str, numbers: List[str]) -> int:
                pass



# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)