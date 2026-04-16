# [Python] 中序遍历改变树的连接（递归）

> Author: Benhao
> Date: 2021-04-25
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
如果有左节点，根将成为左节点生成的根，当前左节点变为None，原来的根成为新的根最右的右子树。

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        if root.left:
            temp = root
            root = self.increasingBST(root.left)
            temp.left = None
            curr = root
            while curr.right:
                curr = curr.right
            curr.right = temp
            temp.right = self.increasingBST(temp.right)
        elif root.right:
            root.right = self.increasingBST(root.right)
        return root
```