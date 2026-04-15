# [Python] 中序遍历

> Author: Benhao
> Date: 2024-03-19
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [98. 验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/description/)

[TOC]

# 思路

> 二叉搜索树中序遍历为递增序列

# 解题方法

> 遍历或递归判断即可

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        return all(a < b for a, b in pairwise(dfs(root)))
```
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_val = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        lr = self.isValidBST(root.left)
        if not lr or root.val <= self.max_val:
            return False
        self.max_val = root.val
        return self.isValidBST(root.right)
```
  
