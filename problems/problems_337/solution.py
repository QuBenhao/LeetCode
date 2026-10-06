import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rob(list_to_tree(test_input))

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0,0
            # Select or skip the left node
            ls, ln = dfs(node.left)
            # Select or skip the right node
            rs, rn = dfs(node.right)
            return node.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(dfs(root))


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
