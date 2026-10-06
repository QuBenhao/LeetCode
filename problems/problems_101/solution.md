# [Python] Recursion

> Author: Benhao
> Date: 2024-03-18
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [101. 对称二叉树](https://leetcode.cn/problems/symmetric-tree/description/)

[TOC]

# Intuition

> Node A's left subtree must match the right subtree of its mirror node B, and A's right subtree must match B's left subtree.

# Approach

> Recursion

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
  
