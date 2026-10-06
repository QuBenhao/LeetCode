# [Python] Iterator

> Author: Benhao
> Date: 2024-03-08
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [230. 二叉搜索树中第K小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/)

[TOC]

# Intuition

> An inorder traversal of a binary search tree yields a sorted sequence; take its kth element.

# Approach

> Use an iterator to avoid traversing the entire tree.

# Complexity

Time complexity:
> $O(k)$

Space complexity:
> $O(k)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if not node:
                return
            yield from dfs(node.left)
            yield node.val
            yield from dfs(node.right)
        
        it = dfs(root)
        for _ in range(k - 1):
            next(it)
        return next(it)
```
  
