import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input
        nums = nums.copy()
        if not nums:
            root = None
        else:
            root = TreeNode(nums.pop(0))
        is_left = True
        curr_nodes = []
        curr_node = root
        while nums:
            num = nums.pop(0)
            if is_left:
                is_left = False
                if num is not None:
                    curr_node.left = TreeNode(val=num)
                    curr_nodes.append(curr_node.left)
                else:
                    curr_node.left = None
            else:
                is_left = True
                if num is not None:
                    curr_node.right = TreeNode(val=num)
                    curr_nodes.append(curr_node.right)
                else:
                    curr_node.right = None
                curr_node = curr_nodes.pop(0)
        return self.rightSideView(root)

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
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


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
