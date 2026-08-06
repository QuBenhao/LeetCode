# [Python] DFS

> slug: python-dfs-by-himymben-2jqi
> date: 2024-03-12
> tags: C, Go, Java, Python3, TypeScript
> question: Find Elements in a Contaminated Binary Tree (find-elements-in-a-contaminated-binary-tree)
> url: https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/solutions/9zwnOy/python-dfs-by-himymben-2jqi/

---

> Problem: [1261. 在受污染的二叉树中查找元素](https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/description/)

[TOC]

# 思路

> 在初始化的时候更新树里的二叉树，将数字维护到集合里

# 解题方法

> 判断是否在集合内即可

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
  
