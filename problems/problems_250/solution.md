# [Python] Postorder traversal

> slug: python-hou-xu-bian-li-by-himymben-swkk
> date: 2021-08-22
> tags: Python, Python3
> question: Count Univalue Subtrees (count-univalue-subtrees)
> url: https://leetcode.cn/problems/count-univalue-subtrees/solutions/ViMd3D/python-hou-xu-bian-li-by-himymben-swkk/

---
### Approach
Use postorder traversal to check whether each node matches the values in its subtrees. If a subtree already contains different values, return inf so that it cannot match its parent.

### Code

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
