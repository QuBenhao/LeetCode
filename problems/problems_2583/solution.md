# [Python/Go/C] BFS

> slug: pythongoc-bfs-by-himymben-agpz
> date: 2024-02-22
> tags: C, Go, Java, Python3, TypeScript
> question: Kth Largest Sum in a Binary Tree (kth-largest-sum-in-a-binary-tree)
> url: https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/solutions/QaJMAh/pythongoc-bfs-by-himymben-agpz/

---

> Problem: [2583. 二叉树中的第 K 大层和](https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/description/)

[TOC]

# Intuition

> Processing the tree one level at a time is a standard use of breadth-first search.

# Approach

> Compute the sum of each level, then sort the sums and return the answer.

# Complexity

Time complexity:
> $O(nlogn)$

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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        queue = deque([root])
        while queue:
            length, s = len(queue), 0
            for _ in range(length):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(s)
        if len(res) < k:
            return -1
        return sorted(res)[-k]
```
```Go []
```
```C []
```
  
