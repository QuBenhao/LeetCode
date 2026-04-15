# [Python] BFS

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 1
> Tags: Python3

---


> Problem: [199. 二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/description/)

[TOC]

# 思路

> BFS

# 解题方法

> BFS

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        while queue:
            ans.append(queue[-1].val)
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans
```
  
