import solution
from object_libs import list_to_tree, list_to_tree_with_target


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target = test_input
        root, target_node = list_to_tree_with_target(nums, target)
        copy_root = list_to_tree(nums)
        return self.getTargetCopy(root, copy_root, target_node).val

    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        nodes = [original]
        nodes_ = [cloned]
        while nodes:
            next_nodes = []
            next_nodes_ = []
            for i in range(len(nodes)):
                if nodes[i] == target:
                    return nodes_[i]
                if nodes[i].left:
                    next_nodes.append(nodes[i].left)
                    next_nodes_.append(nodes_[i].left)
                if nodes[i].right:
                    next_nodes.append(nodes[i].right)
                    next_nodes_.append(nodes_[i].right)
            nodes = next_nodes
            nodes_ = next_nodes_
        return None


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
