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
            # 选了左节点 or 不选左节点
            ls, ln = dfs(node.left)
            # 选了右节点 or 不选右节点
            rs, rn = dfs(node.right)
            return node.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(dfs(root))


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
