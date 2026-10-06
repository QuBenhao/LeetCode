# [Python] Recursion

> Author: Benhao
> Date: 2024-03-23
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/)

[TOC]

# Intuition

> Accumulate the current number during recursion, just as a decimal number is built from left to right: previous number * 10 + current digit.

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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, v):
            nv = 10 * v + node.val
            if not node.left and not node.right:
                return nv
            ans = 0
            if node.left:
                ans += dfs(node.left, nv)
            if node.right:
                ans += dfs(node.right, nv)
            return ans

        return dfs(root, 0)
```
  
