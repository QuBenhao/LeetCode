import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, x, y = test_input
        root = list_to_tree(nums)
        return self.isCousins(root, x, y)

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        frontier = {root:None}
        fx = fy = None
        while frontier:
            new = dict()
            for node in frontier:
                if node.val == x:
                    fx = frontier[node]
                if node.val == y:
                    fy = frontier[node]
                if node.left:
                    new[node.left] = node
                if node.right:
                    new[node.right] = node
            if fx is not None or fy is not None:
                if fx is None or fy is None:
                    return False
                return fx != fy
            frontier = new
        return False


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
