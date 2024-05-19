import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, nums2 = test_input
        root1, root2 = list_to_tree(nums1), list_to_tree(nums2)
        return self.leafSimilar(root1, root2)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return
            if not root.left and not root.right:
                yield root.val
                return
            yield from dfs(root.left)
            yield from dfs(root.right)

        return list(dfs(root1)) == list(dfs(root2))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
