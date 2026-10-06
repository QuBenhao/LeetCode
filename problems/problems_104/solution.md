# [Python] Recursion

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)

[TOC]

# Intuition

> Recurse through the tree.

# Approach

> Take the greater of the left and right subtree depths, then add the depth contributed by the current node.

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
```
  
