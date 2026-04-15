# [Python] 递归

> Author: Benhao
> Date: 2024-03-02
> Upvotes: 2
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [108. 将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)

[TOC]

# 思路

> 要平衡每次从中间分是最好的选择

# 解题方法

> 这里直接选择切数组，实际上用坐标最好，节省空间

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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return TreeNode(nums[n//2], self.sortedArrayToBST(nums[:n//2]), self.sortedArrayToBST(nums[n//2+1:])) if (n := len(nums)) > 0 else None
```
  
