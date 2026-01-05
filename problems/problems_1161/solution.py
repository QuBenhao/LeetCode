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
        return self.maxLevelSum(root0)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans, ans_x = -inf, 0
        cur = 1
        while q:
            sz = len(q)
            s = 0
            for _ in range(sz):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if s > ans:
                ans, ans_x = s, cur
            cur += 1
        return ans_x
