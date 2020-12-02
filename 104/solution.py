import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root_nums = test_input

        def insertLevelOrder(arr, root, i, n):
            # Base case for recursion
            if i < n:
                temp = TreeNode(arr[i])
                root = temp

                # insert left child
                root.left = insertLevelOrder(arr, root.left,
                                             2 * i + 1, n)

                # insert right child
                root.right = insertLevelOrder(arr, root.right,
                                              2 * i + 2, n)
            return root
        root = insertLevelOrder(root_nums, None, 0, len(root_nums))

        return self.maxDepth(root)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(node, d):
            if not node:
                return d
            if not node.left and not node.right:
                return d + 1
            d += 1
            return max(depth(node.left, d), depth(node.right, d))

        return depth(root, 0)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
