# [Python] 使用字典的BFS 

> Author: Benhao
> Date: 2021-05-16
> Upvotes: 1
> Tags: Python, Python3

---

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        frontier = {root:None}
        fx = fy = None
        while frontier:
            new = dict()
            for node in frontier:
                if node.val == x:
                    fx = frontier[node]
                if node.val == y:
                    fy = frontier[node]
                if node.left:
                    new[node.left] = node
                if node.right:
                    new[node.right] = node
            if fx is not None or fy is not None:
                if fx is None or fy is None:
                    return False
                return fx != fy
            frontier = new
        return False
```