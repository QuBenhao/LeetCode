import solution


class Solution(solution.Solution):

    def solve(self, test_input=None):
        root_nums = list(test_input)
        root = TreeNode(root_nums.pop(0))
        while root_nums:
            last = curr = root
            num = root_nums.pop(0)
            if num is not None:
                L = False
                while curr:
                    if num < curr.val:
                        last = curr
                        curr = curr.left
                        L = True
                    else:
                        last = curr
                        curr = curr.right
                        L = False
                if L:
                    last.setL(TreeNode(val=num))
                else:
                    last.setR(TreeNode(val=num))
        self.res = float("inf")
        self.pre = -float("inf")
        return self.minDiffInBST(root)

    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return

        self.minDiffInBST(root.left)
        # evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        self.minDiffInBST(root.right)
        return self.res

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def setL(self, left):
        self.left = left

    def setR(self, right):
        self.right = right
