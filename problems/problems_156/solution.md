# [Python] 递归解法

> slug: python-di-gui-jie-fa-by-himymben-os72
> date: 2021-08-21
> tags: Python, Python3
> question: Binary Tree Upside Down (binary-tree-upside-down)
> url: https://leetcode.cn/problems/binary-tree-upside-down/solutions/3yaKHJ/python-di-gui-jie-fa-by-himymben-os72/

---
### 解题思路
函数返回最终的root，也就是没有root.left的地方。
更改顺序为递归，先从最后的root开始整理，递归到最左节点，根的右节点为原来的父节点，根的左节点为原来的右节点。依次递归

### 代码

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