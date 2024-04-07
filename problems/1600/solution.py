import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ThroneInheritance(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class ThroneInheritance:

    def __init__(self, kingName: str):
        pass

    def birth(self, parentName: str, childName: str) -> None:
        pass

    def death(self, name: str) -> None:
        pass

    def getInheritanceOrder(self) -> List[str]:
        pass

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
