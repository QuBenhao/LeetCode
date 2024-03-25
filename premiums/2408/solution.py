import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = SQL(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
            pass


    def insertRow(self, name: str, row: List[str]) -> None:
            pass


    def deleteRow(self, name: str, rowId: int) -> None:
            pass


    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
                pass



# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)