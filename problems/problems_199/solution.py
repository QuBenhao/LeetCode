import solution
from python.object_libs import list_to_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.rightSideView(root)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # def dfs(root, level):
        #     if not root:
        #         return
        #     if level == len(ans):
        #         ans.append(root.val)
        #     dfs(root.right, level + 1)
        #     dfs(root.left, level + 1)
        #
        # ans = []
        # dfs(root, 0)
        # return ans

        ans = []
        if not root:
            return ans
        nodes = [root]
        while nodes:
            ans.append(nodes[-1].val)
            next_nodes = []
            for node in nodes:
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)
            nodes = next_nodes
        return ans
