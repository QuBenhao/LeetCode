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
            # 每个节点有 不染色 到 处于染了k个色的连接之中 的所有情况
            dp = [0] * (k + 1)
            if not node:
                return dp
            left = dfs(node.left)
            right = dfs(node.right)
            # 当前不涂色，左右两边的结果全部可以获得
            dp[0] = max(left) + max(right)
            # 当前涂色
            for i in range(1, k + 1):
                # 左边涂j个色，右边涂i-1-j
                dp[i] = max(left[j] + right[i - 1 - j] for j in range(i)) + node.val
            return dp

        return max(dfs(root))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
