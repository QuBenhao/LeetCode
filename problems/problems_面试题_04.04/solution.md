# [Python] 递归

> slug: python-di-gui-by-himymben-sn9r
> date: 2022-03-14
> tags: Python, Python3
> question: Check Balance LCCI (check-balance-lcci)
> url: https://leetcode.cn/problems/check-balance-lcci/solutions/17RbNd/python-di-gui-by-himymben-sn9r/

---
### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def high(node):
            if not node:
                return 0, True
            l = high(node.left)
            r = high(node.right)
            return max(l[0], r[0]) + 1, l[1] and r[1] and abs(l[0] - r[0]) <= 1
        
        if not root:
            return True
        l = high(root.left)
        r = high(root.right)
        if l[1] and r[1] and abs(l[0] - r[0]) <= 1:
            return True
        return False

```