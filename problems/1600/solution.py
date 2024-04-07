import solution
from typing import *
from object_libs import call_method
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ThroneInheritance(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = kingName
        self.tree = defaultdict(list)
        self.deleted = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deleted.add(name)

    def getInheritanceOrder(self) -> List[str]:
        def preorder(node):
            if node not in self.deleted:
                yield node
            for child in self.tree[node]:
                yield from preorder(child)

        return list(preorder(self.root))

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
