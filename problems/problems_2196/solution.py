import solution
from typing import *
from python.object_libs import tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        descriptions = test_input
        res = self.createBinaryTree(descriptions)
        return tree_to_list(res)

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # Map node values to nodes with a hash table
        nodes = {}
        # Record all child nodes to find the root
        children = set()

        for parent_val, child_val, is_left in descriptions:
            # Ensure the parent node exists
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            # Ensure the child node exists
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

            # Establish the parent-child relationship
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

            # Record the child node
            children.add(child_val)

        # The root is the node absent from the children set
        for val in nodes:
            if val not in children:
                return nodes[val]

        return None

