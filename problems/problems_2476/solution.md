# [Python] 中序遍历+二分查找

> slug: python-zhong-xu-bian-li-er-fen-cha-zhao-6uitw
> date: 2024-02-24
> tags: C, Go, Java, Python3, TypeScript
> question: Closest Nodes Queries in a Binary Search Tree (closest-nodes-queries-in-a-binary-search-tree)
> url: https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/hFEiPg/python-zhong-xu-bian-li-er-fen-cha-zhao-6uitw/

---

> Problem: [2476. 二叉搜索树最近节点查询](https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/description/)

[TOC]

# 思路

> 二叉搜索树可以通过中序遍历得到顺序，针对每个查询可以找到它前后的元素

# 解题方法

> 二分查找有序数组

# 复杂度

时间复杂度:
> $O(n+qlogn)$

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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return [[arr[-1], -1] if (l:=bisect_left(arr, q)) >= len(arr) else [arr[l] if arr[l] == q else (-1 if l == 0 else arr[l-1]), arr[l]] for q in queries]
```
  
