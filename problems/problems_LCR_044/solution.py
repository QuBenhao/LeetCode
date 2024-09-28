from collections import deque
from math import inf

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
        return self.largestValues(root0)

    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            size = len(q)
            max_val = -inf
            for _ in range(size):
                node = q.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_val)
        return ans
