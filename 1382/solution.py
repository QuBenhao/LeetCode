import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input
        nums = nums.pop(0)[0]
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

        return self.balanceBST(root)

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            nodes.append(node)
            in_order(node.right)

        in_order(root)

        def construct_AVL(nodes):
            if not nodes:
                return
            mid = len(nodes) // 2
            node = nodes[mid]
            node.left = construct_AVL(nodes[:mid])
            node.right = construct_AVL(nodes[mid+1:])
            return node

        return construct_AVL(nodes)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
