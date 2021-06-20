import solution
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        # Your ThroneInheritance object will be instantiated and called as such:
        # obj = ThroneInheritance(kingName)
        # obj.birth(parentName,childName)
        # obj.death(name)
        # param_3 = obj.getInheritanceOrder()
        ops, vals = test_input
        ans = [None]
        obj = ThroneInheritance(vals[0][0])
        for i in range(1, len(ops)):
            if ops[i] == "birth":
                parent, child = vals[i]
                obj.birth(parent, child)
                ans.append(None)
            elif ops[i] == "death":
                obj.death(vals[i][0])
                ans.append(None)
            else:
                ans.append(obj.getInheritanceOrder())
        return ans


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
