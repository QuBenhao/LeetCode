from collections import deque

import solution
from typing import *
from python.object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.widthOfBinaryTree(root0)

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        q = deque([(0, root)])
        while q:
            ans = max(ans, q[-1][0] - q[0][0] + 1)
            for _ in range(len(q)):
                idx, node = q.popleft()
                if node.left:
                    q.append((2 * idx, node.left))
                if node.right:
                    q.append((2 * idx + 1, node.right))
        return ans
