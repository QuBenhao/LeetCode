import solution
from typing import *
from python.object_libs import list_to_tree


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
                # Compute the maximum depth of the subtree rooted at start
                # Unlike method 1, there is no +1 after max, so this also computes the maximum depth
                ans = max(l_len, r_len)
                return 1, True  # Found start
            if l_found or r_found:
                # Update the answer only when the left or right subtree contains start
                ans = max(ans, l_len + r_len)  # Join the two chains into a diameter
                # Ensure start is an endpoint of the diameter
                return (l_len if l_found else r_len) + 1, True
            return max(l_len, r_len) + 1, False

        dfs(root)
        return ans
