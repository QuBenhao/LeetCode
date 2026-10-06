# [Python] Rewire the tree with inorder traversal (recursion)

> Author: Benhao
> Date: 2021-04-25
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
If there is a left child, the new root is the root produced from that child. Set the current left child to None and attach the original root as the rightmost right subtree of the new root.

### Code

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
