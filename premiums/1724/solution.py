import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = DistanceLimitedPathsExist(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class DistanceLimitedPathsExist:

    def __init__(self, n: int, edgeList: List[List[int]]):
            pass


    def query(self, p: int, q: int, limit: int) -> bool:
                pass



# Your DistanceLimitedPathsExist object will be instantiated and called as such:
# obj = DistanceLimitedPathsExist(n, edgeList)
# param_1 = obj.query(p,q,limit)