import solution
from collections import deque
from python.object_libs import list_to_tree, tree_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        # Your Codec object will be instantiated and called as such:
        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(root))
        return tree_to_list(ans)


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
                    curr_node.left = TreeNode(int(num))
                    curr_nodes.append(curr_node.left)
            else:
                left = True
                if num != '#':
                    curr_node.right = TreeNode(int(num))
                    curr_nodes.append(curr_node.right)
                curr_node = curr_nodes.popleft()
        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
