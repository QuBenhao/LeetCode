# [Python] 递归

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [104. 二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)

[TOC]

# 思路

> 树的递归即可

# 解题方法

> 左子树深度和右子树深度更大的一个加上自身深度

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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
```
  
