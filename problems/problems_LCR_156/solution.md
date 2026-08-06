# [Python] BFS

> slug: python-an-ceng-die-dai-by-qubenhao-ka3u
> date: 2021-06-30
> tags: Python, Python3
> question: 序列化与反序列化二叉树 (xu-lie-hua-er-cha-shu-lcof)
> url: https://leetcode.cn/problems/xu-lie-hua-er-cha-shu-lcof/solutions/3atZcy/python-an-ceng-die-dai-by-qubenhao-ka3u/

---
### 解题思路
用一个特殊符号表示空，题目给的例子是按root->root.left->root.right的顺序依次入队，其实就是BFS。

反序列化的时候左右交替
<br>
今天是六月最后一天，正好也是刷的第500道题。坚持就有收获。

### 代码

```python3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            if not node:
                ans.append('#')
            else:
                ans.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        while ans and ans[-1] == '#':
            ans.pop()
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root_nums = data.split(',')
        if not root_nums or root_nums[0] == '#' or root_nums[0] == '':
            return None
        root_nums = deque(root_nums)
        root = TreeNode(int(root_nums.popleft()))
        left = True
        curr_nodes = deque([])
        curr_node = root
        while root_nums:
            num = root_nums.popleft()
            if left:
                left = False
                if num != '#':
                    curr_node.left = TreeNode(val=int(num))
                    curr_nodes.append(curr_node.left)
            else:
                left = True
                if num != '#':
                    curr_node.right = TreeNode(val=int(num))
                    curr_nodes.append(curr_node.right)
                curr_node = curr_nodes.popleft()
        return root

 

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```