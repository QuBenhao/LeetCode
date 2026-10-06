# [Python] Recursive solution

> slug: python-di-gui-jie-fa-by-himymben-os72
> date: 2021-08-21
> tags: Python, Python3
> question: Binary Tree Upside Down (binary-tree-upside-down)
> url: https://leetcode.cn/problems/binary-tree-upside-down/solutions/3yaKHJ/python-di-gui-jie-fa-by-himymben-os72/

---
### Approach
The function returns the final root: the node with no root.left.
Reorder the tree recursively, starting from the final root. Recurse to the leftmost node; the root's right child becomes its original parent, and its left child becomes the original right node. Repeat through the recursion.

### Code

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root or not root.left:
            return root
        tmpL, tmpR = root.left, root.right
        res = self.upsideDownBinaryTree(root.left)
        root.left = root.right = None
        tmpL.left = tmpR
        tmpL.right = root
        return res

```
