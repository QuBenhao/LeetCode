# [Python] Inorder traversal + binary search

> slug: python-zhong-xu-bian-li-er-fen-cha-zhao-6uitw
> date: 2024-02-24
> tags: C, Go, Java, Python3, TypeScript
> question: Closest Nodes Queries in a Binary Search Tree (closest-nodes-queries-in-a-binary-search-tree)
> url: https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/solutions/hFEiPg/python-zhong-xu-bian-li-er-fen-cha-zhao-6uitw/

---

> Problem: [2476. 二叉搜索树最近节点查询](https://leetcode.cn/problems/closest-nodes-queries-in-a-binary-search-tree/description/)

[TOC]

# Intuition

> An inorder traversal of a binary search tree yields sorted values, allowing us to find the neighboring elements for each query.

# Approach

> Binary-search the sorted array.

# Complexity

Time complexity:
> $O(n+qlogn)$

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
  
