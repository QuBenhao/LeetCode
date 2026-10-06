# [Python] DFS

> slug: python-dfs-by-himymben-2jqi
> date: 2024-03-12
> tags: C, Go, Java, Python3, TypeScript
> question: Find Elements in a Contaminated Binary Tree (find-elements-in-a-contaminated-binary-tree)
> url: https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/solutions/9zwnOy/python-dfs-by-himymben-2jqi/

---

> Problem: [1261. 在受污染的二叉树中查找元素](https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/description/)

[TOC]

# Intuition

> Restore the binary tree during initialization and store its values in a set.

# Approach

> Then check membership in the set.

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
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        s = set()
        def dfs(root):
            if not root:
                return
            s.add(root.val)
            if root.left:
                root.left.val = root.val * 2 + 1
                dfs(root.left)
            if root.right:
                root.right.val = root.val * 2 + 2
                dfs(root.right)
        root.val = 0
        dfs(root)
        self.s = s



    def find(self, target: int) -> bool:
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
```
  
