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
        return self.rightSideView(root0)

    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        q = deque([root])
        while q:
            n = len(q)
            ans.append(q[0].val)
            for _ in range(n):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return ans
