import solution
from typing import *
from object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, start = test_input
        root0 = list_to_tree(nums0)
        return self.amountOfTime(root0, start)

    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> (int, bool):
            if node is None:
                return 0, False
            l_len, l_found = dfs(node.left)
            r_len, r_found = dfs(node.right)
            nonlocal ans
            if node.val == start:
                # 计算子树 start 的最大深度
                # 注意这里和方法一的区别，max 后面没有 +1，所以算出的也是最大深度
                ans = max(l_len, r_len)
                return 1, True  # 找到了 start
            if l_found or r_found:
                # 只有在左子树或右子树包含 start 时，才能更新答案
                ans = max(ans, l_len + r_len)  # 两条链拼成直径
                # 保证 start 是直径端点
                return (l_len if l_found else r_len) + 1, True
            return max(l_len, r_len) + 1, False

        dfs(root)
        return ans
