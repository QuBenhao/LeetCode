# [Python] Preorder tree traversal (yield)

> Author: Benhao
> Date: 2021-06-20
> Upvotes: 5
> Tags: Python, Python3

---

### Approach
The priority order returned by Successor is:
Current node > its leftmost child > its second child from the left > ... > its last child

This is a preorder traversal and a chance to practice yield.

### Code

```python3
class ThroneInheritance:
    def __init__(self, kingName: str):
        self.root = kingName
        # parent -> alive, children
        self.tree = {kingName:[True, []]}

    def birth(self, parentName: str, childName: str) -> None:
        self.tree[parentName][1].append(childName)
        self.tree[childName] = [True, []]

    def death(self, name: str) -> None:
        self.tree[name][0] = False

    def getInheritanceOrder(self) -> List[str]:
        def preOrder(node):
            if self.tree[node][0]:
                yield node
            for child in self.tree[node][1]:
                yield from preOrder(child)
        return list(preOrder(self.root))
```
A set can track deceased people, keeping the tree structure simple.
```python3
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
```
