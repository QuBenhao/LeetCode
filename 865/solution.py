import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums = test_input
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

        node = self.subtreeWithAllDeepest(root)
        arr = []
        last = [node]
        while last:
            node = last.pop(0)
            arr.append(node.val)
            if node.left:
                last.append(node.left)
            if node.right:
                last.append(node.right)
        return arr

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def search(node):
            if not node:
                return None, 0
            l_node, l_depth = search(node.left)
            r_node, r_depth = search(node.right)

            if l_depth == r_depth:
                return node, l_depth + 1
            elif l_depth < r_depth:
                return r_node, r_depth + 1
            else:
                return l_node, l_depth + 1

        node, _ = search(root)

        return node


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
