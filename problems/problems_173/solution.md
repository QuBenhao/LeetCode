# [Python] Stack

> Author: Benhao
> Date: 2021-03-27
> Upvotes: 6
> Tags: Python

---

### Approach
At each step, push only the path from the current node to its leftmost leaf onto the stack, so nodes are popped before their parents.
After popping a node, treat its right child, if any, as the root of a smaller tree and push its path onto the stack.

### Code

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
