import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = SnapshotArray(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class SnapshotArray:

    def __init__(self, length: int):
        pass


    def set(self, index: int, val: int) -> None:
            pass


    def snap(self) -> int:
        pass


    def get(self, index: int, snap_id: int) -> int:
            pass



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)