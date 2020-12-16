import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input.copy()
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
        return self.isValidBST(root)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(root,minv,maxv):
            if not root:
                return True
            if minv is not None:
                if root.val <= minv:
                    return False
            if maxv is not None:
                if root.val >= maxv:
                    return False
            return valid(root.left,minv,root.val) and valid(root.right,root.val,maxv)

        return valid(root,None,None)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
