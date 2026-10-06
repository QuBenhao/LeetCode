# [Python] Recursion

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)

[TOC]

# Intuition

> Splitting at the middle each time is the best choice for keeping the tree balanced.

# Approach

> This implementation slices the array directly. Using indices would be better because it saves space.

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return TreeNode(nums[n//2], self.sortedArrayToBST(nums[:n//2]), self.sortedArrayToBST(nums[n//2+1:])) if (n := len(nums)) > 0 else None
```
  
