# [Python] BFS

> Author: Benhao
> Date: 2024-04-03
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [1379. 找出克隆二叉树中的相同节点](https://leetcode.cn/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/description/)

[TOC]

# Intuition

> Traverse the original and cloned nodes together with BFS; return cloned when target is reached.

# Approach

> BFS

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original, cloned)])
        while q:
            o, c = q.popleft()
            if o == target:
                return c
            if o.left:
                q.append((o.left, c.left))
            if o.right:
                q.append((o.right, c.right))
```
  
