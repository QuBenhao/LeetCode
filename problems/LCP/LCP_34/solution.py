import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root_nums, k = test_input

        def insertLevelOrder(arr, root, i, n):
            # Base case for recursion
            if i < n:
                if arr[i] is None:
                    return None
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
        return self.maxValue(root, k)

    def maxValue(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def dfs(node):
            # Each node has states ranging from uncolored to belonging to a connected component of k colored nodes
            dp = [0] * (k + 1)
            if not node:
                return dp
            left = dfs(node.left)
            right = dfs(node.right)
            # Leave the current node uncolored and take the best results from both subtrees
            dp[0] = max(left) + max(right)
            # Color the current node
            for i in range(1, k + 1):
                # Color j nodes on the left and i-1-j on the right
                dp[i] = max(left[j] + right[i - 1 - j] for j in range(i)) + node.val
            return dp

        return max(dfs(root))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
