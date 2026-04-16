# [Python] 递归

> Author: Benhao
> Date: 2024-03-23
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [129. 求根节点到叶节点数字之和](https://leetcode.cn/problems/sum-root-to-leaf-numbers/description/)

[TOC]

# 思路

> 在递归的同时累加当前数字，就和十进制从左到右遍历构成数是一个道理，上一次的数*10+当前数

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
  
