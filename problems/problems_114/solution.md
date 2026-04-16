# [Python] 递归

> Author: Benhao
> Date: 2024-03-19
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [114. 二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/)

[TOC]

# 思路

> 递归处理子树，重新拼接

# 解题方法

> 将左子树变为右子树，右子树接到左子树变化后最右下

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
