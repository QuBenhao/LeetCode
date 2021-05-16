import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root_nums = test_input

        def insertLevelOrder(arr, root, i, n):
            # Base case for recursion
            if i < n:
                if not arr[i]:
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

        return self.rob(root)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return 0,0
            # 选了左节点 or 不选左节点
            ls, ln = dfs(node.left)
            # 选了右节点 or 不选右节点
            rs, rn = dfs(node.right)
            return node.val + ln + rn, max(ls, ln) + max(rs, rn)
        return max(dfs(root))


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
