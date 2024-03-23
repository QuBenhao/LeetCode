import solution
from collections import defaultdict
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        # Your ThroneInheritance object will be instantiated and called as such:
        # obj = ThroneInheritance(kingName)
        # obj.birth(parentName,childName)
        # obj.death(name)
        # param_3 = obj.getInheritanceOrder()
        ops, inputs = test_input
        obj = ThroneInheritance(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class ThroneInheritance(object):

    def __init__(self, kingName):
        """
        :type kingName: str
        """
        self.root = kingName
        # parent -> children
        self.tree = defaultdict(list)
        self.deads = set()

    def birth(self, parentName, childName):
        """
        :type parentName: str
        :type childName: str
        :rtype: None
        """
        self.tree[parentName].append(childName)

    def death(self, name):
        """
        :type name: str
        :rtype: None
        """
        self.deads.add(name)

    def getInheritanceOrder(self):
        """
        :rtype: List[str]
        """
        """
        Successor(x, curOrder):
        如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
            如果 x 是国王，那么返回 null
            否则，返回 Successor(x 的父亲, curOrder)
        否则，返回 x 不在 curOrder 中最年长的孩子
        """
        def preOrder(node):
            if node not in self.deads:
                yield node
            if node in self.tree:
                for child in self.tree[node]:
                    yield from preOrder(child)
        return list(preOrder(self.root))
