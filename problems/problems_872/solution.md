# [Python] 迭代使用yield

> Author: Benhao
> Date: 2021-05-10
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
借着二叉树练练yield和yield from

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
                return
            yield from dfs(root.left)
            yield from dfs(root.right)
        return all(a == b for a, b in itertools.zip_longest(dfs(root1), dfs(root2)))

```