# [Python] BFS

> slug: python-bfs-by-himymben-xai4
> date: 2024-03-08
> tags: C, Go, Java, Python3, TypeScript
> question: Average of Levels in Binary Tree (average-of-levels-in-binary-tree)
> url: https://leetcode.cn/problems/average-of-levels-in-binary-tree/solutions/Hde91S/python-bfs-by-himymben-xai4/

---

> Problem: [637. 二叉树的层平均值](https://leetcode.cn/problems/average-of-levels-in-binary-tree/description/)

[TOC]

# Intuition

> Whenever a problem operates on each level, consider BFS first. In languages where overflow is possible, consider dividing first and accumulating fractional values.

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
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque([root])
        while queue:
            s = 0
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(s / length)
        return ans
```
  
