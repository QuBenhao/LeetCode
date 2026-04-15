# [Python] 递归

> Author: Benhao
> Date: 2024-03-18
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/description/)

[TOC]

# 思路

> A节点的左子树要和对称的B节点的右子树一致，A节点的右子树要和对称的B节点的左子树一致

# 解题方法

> 递归

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(n1, n2):
            if not n1 and not n2:
                return True
            return n1 is not None and n2 is not None and n1.val == n2.val and check(n1.left, n2.right) and check(n1.right, n2.left)
        
        return check(root, root)
```
  
