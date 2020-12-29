import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input.copy()
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
        return self.pseudoPalindromicPaths(root)

    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def count_traversal(node, vals):
            if node.val in vals:
                vals.remove(node.val)
            else:
                vals.append(node.val)

            if not node.left and not node.right:
                if len(vals) < 2:
                    self.count += 1
                return
            if node.left:
                count_traversal(node.left, list(vals))
            if node.right:
                count_traversal(node.right, list(vals))

        count_traversal(root, [])
        return self.count


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
