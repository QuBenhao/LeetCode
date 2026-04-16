# [Python] 递归

> Author: Benhao
> Date: 2024-03-20
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [112. 路径总和](https://leetcode.cn/problems/path-sum/description/)

[TOC]

# 思路

> 首先想到递归的时候减去当前节点的值(即为加入和)，向下寻找能否在叶子节点的时候和为0。但是要特别注意空节点不代表和为0

# 解题方法

> 判断当前节点和是否为叶子节点，递归处理和

# 复杂度

时间复杂度:
> 添加时间复杂度, 示例： $O(n)$

空间复杂度:
> 添加空间复杂度, 示例： $O(n)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if not root.left and not root.right:
            return targetSum == 0
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
```
  
