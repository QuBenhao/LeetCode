import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = list(test_input)
        root = TreeNode(nums.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num:
                    curr_node.left = TreeNode(val=num)
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num:
                    curr_node.right = TreeNode(val=num)
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        return self.findSecondMinimumValue(root)

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
