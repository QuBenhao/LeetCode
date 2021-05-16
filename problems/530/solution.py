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
        return self.getMinimumDifference(root)

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def in_order(prev, curr, m):
            if not curr:
                return prev, m
            prev, m = in_order(prev, curr.left, m)
            m, prev = min(m, curr.val - prev), curr.val
            return in_order(prev, curr.right, m)

        return in_order(-float("inf"),root,float("inf"))[1]


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
