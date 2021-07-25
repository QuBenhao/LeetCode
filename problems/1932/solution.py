import solution
from collections import deque, defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        trees = []
        for lt in test_input:
            root = TreeNode(lt[0])
            for i in range(1, len(lt)):
                if lt[i] < lt[0]:
                    root.left = TreeNode(lt[i])
                else:
                    root.right = TreeNode(lt[i])
            trees.append(root)
        root = self.canMerge(trees)
        ans = []
        q = deque([root])
        while q:
            node = q.popleft()
            if not node:
                ans.append(None)
                continue
            ans.append(node.val)
            q.append(node.left)
            q.append(node.right)
        while ans and ans[-1] is None:
            ans.pop()
        return ans

    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
