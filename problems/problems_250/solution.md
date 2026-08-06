# [Python] 后序遍历

> slug: python-hou-xu-bian-li-by-himymben-swkk
> date: 2021-08-22
> tags: Python, Python3
> question: Count Univalue Subtrees (count-univalue-subtrees)
> url: https://leetcode.cn/problems/count-univalue-subtrees/solutions/ViMd3D/python-hou-xu-bian-li-by-himymben-swkk/

---
### 解题思路
后序遍历，检查节点与子树节点值是否一致，如果子树已经不一致，返回inf，这样可以保证他们值(与父节点)不相同

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return None
            if not node.left and not node.right:
                self.ans += 1
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left == right == node.val or (left is None and right == node.val) or (right is None and left == node.val):
                self.ans += 1
                return node.val
            return inf
        
        dfs(root)
        return self.ans

```