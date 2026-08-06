# [Python/Go/C] BFS

> slug: pythongoc-bfs-by-himymben-agpz
> date: 2024-02-22
> tags: C, Go, Java, Python3, TypeScript
> question: Kth Largest Sum in a Binary Tree (kth-largest-sum-in-a-binary-tree)
> url: https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/solutions/QaJMAh/pythongoc-bfs-by-himymben-agpz/

---

> Problem: [2583. 二叉树中的第 K 大层和](https://leetcode.cn/problems/kth-largest-sum-in-a-binary-tree/description/)

[TOC]

# 思路

> 要依次对树的每一层做操作，这是标准的广度优先搜索。

# 解题方法

> 逐层统计每层的和，最后排序返回答案

# 复杂度

时间复杂度:
> $O(nlogn)$

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
  
