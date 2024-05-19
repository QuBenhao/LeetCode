import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findSecondMinimumValue(list_to_tree(test_input))

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 必然不存在第二小的值
        if not root or not root.left:
            return -1
        # 我们知道root.val是最小值，那么,
        # 第二小的值存在于 更小的子节点那一边的子树的第二小的值 或 更大的子节点 之中
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        return min(left, right) if left != -1 and right != -1 else max(left, right)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
