# [Python] 找到根，从根递归构建

> slug: python-zhao-dao-gen-cong-gen-di-gui-gou-4wkoq
> date: 2022-03-06
> tags: Python, Python3
> question: Create Binary Tree From Descriptions (create-binary-tree-from-descriptions)
> url: https://leetcode.cn/problems/create-binary-tree-from-descriptions/solutions/GiLTQG/python-zhao-dao-gen-cong-gen-di-gui-gou-4wkoq/

---
### 解题思路
根是出现在parent里没出现在child里的

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        lefts, rights = dict(), dict()
        s1, s2 = set(), set()
        for p, c, l in descriptions:
            s1.add(p)
            s2.add(c)
            if l:
                lefts[p] = c
            else:
                rights[p] = c
        rVal = (s1 - s2).pop()
        root = TreeNode(rVal)
        
        def dfs(node):
            v = node.val
            if v in lefts:
                node.left = TreeNode(lefts[v])
                dfs(node.left)
            if v in rights:
                node.right = TreeNode(rights[v])
                dfs(node.right)
        
        dfs(root)
        return root
```