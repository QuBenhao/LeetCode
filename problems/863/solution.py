import solution
from typing import *
from object_libs import list_to_tree_with_target


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, target_val, k = test_input
        root, target = list_to_tree_with_target(nums, target_val)
        return self.distanceK(root, target, k)

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        elif k > 501:
            return []

        def dfs1(node):
            if not node:
                return []
            if node == target:
                return [node]
            left = dfs1(node.left)
            if left:
                left.append(node)
                return left
            right = dfs1(node.right)
            if right:
                right.append(node)
            return right

        dists = dfs1(root)
        parents_distance = dict()
        for i, node in enumerate(dists):
            parents_distance[node] = i

        ans = []

        def dfs2(node, dis):
            if not node:
                return
            if node in parents_distance:
                dis = k - parents_distance[node]
            if dis < 0 and not (
                    (node.left and node.left in parents_distance) or (node.right and node.right in parents_distance)):
                return
            if not dis:
                ans.append(node.val)
            dfs2(node.left, dis - 1)
            dfs2(node.right, dis - 1)

        dfs2(root, k)
        return ans
