# [Python] Recursion

> Author: Benhao
> Date: 2024-04-04
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [1026. 节点与其祖先之间的最大差值](https://leetcode.cn/problems/maximum-difference-between-node-and-ancestor/description/)

[TOC]

# Intuition

> Track the maximum and minimum ancestor values during recursion; the answer is among the absolute differences from these values.

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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, mx, mn):
            if not node:
                return 0
            cur = max(mx - node.val, node.val - mn)
            mx, mn = max(node.val, mx), min(node.val, mn)
            left, right = helper(node.left, mx, mn), helper(node.right, mx, mn)
            return max(cur, left, right)
        
        return helper(root, root.val, root.val)
```
  
