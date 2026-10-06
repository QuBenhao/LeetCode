# [Python] Recursion

> Author: Benhao
> Date: 2024-03-19
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/)

[TOC]

# Intuition

> Process the subtrees recursively, then reconnect them.

# Approach

> Move the left subtree to the right, then attach the original right subtree to the bottom-right end of the transformed left subtree.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        right = root.right
        self.flatten(root.left)
        self.flatten(root.right)
        root.left, root.right = None, root.left
        node = root
        while node.right:
            node = node.right
        node.right = right
```
  
