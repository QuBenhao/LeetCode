# [Python] 栈

> Author: Benhao
> Date: 2021-03-27
> Upvotes: 6
> Tags: Python

---

### 解题思路
每次只存储当前到其最左的左叶子节点到栈中，这样pop的顺序就是在子节点优于父节点。
而pop以后，将被pop的节点的右节点（如果有）作为一个相当于小的树的根节点来压入栈中。

### 代码

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.in_order(root)
    
    def in_order(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.in_order(node.right)
        
        return node.val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return bool(self.stack)



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```