# [Python] Recursion

> Author: Benhao
> Date: 2024-03-20
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [112. 路径总和](https://leetcode.cn/problems/path-sum/description/)

[TOC]

# Intuition

> The first idea is to subtract the current node's value during recursion, accounting for it in the sum, and continue downward to see whether the remaining sum is 0 at a leaf. Be careful: reaching a null node does not mean the sum is 0.

# Approach

> Check the current node's value and whether it is a leaf, then process the remaining sum recursively.

# Complexity

Time complexity:
> Add the time complexity, for example: $O(n)$

Space complexity:
> Add the space complexity, for example: $O(n)$



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
  
