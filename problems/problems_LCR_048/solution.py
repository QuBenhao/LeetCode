import solution
from typing import *
from python.object_libs import call_method, list_to_tree, tree_to_list


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        obj = Codec()
        serial = obj.serialize(root)
        return tree_to_list(obj.deserialize(serial))


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def preorder(node):
            if not node:
                ans.append("#")
                return
            ans.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)
        while ans and ans[-1] == "#":
            ans.pop()
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        preorder_list = data.split(",")
        idx = 0

        def build() -> Optional[TreeNode]:
            nonlocal idx
            if idx >= len(preorder_list) or preorder_list[idx] == "#":
                idx += 1
                return None
            root = TreeNode(int(preorder_list[idx]))
            idx += 1
            root.left = build()
            root.right = build()
            return root

        return build()
