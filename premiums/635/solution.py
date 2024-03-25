import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = LogSystem()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class LogSystem:

    def __init__(self):
        pass


    def put(self, id: int, timestamp: str) -> None:
            pass


    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
                pass



# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)