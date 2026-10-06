import solution
from typing import *
from python.object_libs import list_to_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums_arr = test_input
        roots = [list_to_tree(nums) for nums in nums_arr]
        res = self.canMerge(roots)
        return tree_to_list(res)

    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # Hash set of all leaf values
        leaves = set()
        # Hash map from root values to trees
        candidates = dict()
        for tree in trees:
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
            candidates[tree.val] = tree

        # Previous inorder value, used to check strict increase
        prev = float("-inf")

        # Inorder traversal; return whether values are strictly increasing
        def dfs(tree: Optional[TreeNode]) -> bool:
            if not tree:
                return True

            # Merge when a leaf has a matching tree available
            if not tree.left and not tree.right and tree.val in candidates:
                tree.left = candidates[tree.val].left
                tree.right = candidates[tree.val].right
                # Remove the merged tree from the map so we can later check that every tree was visited
                candidates.pop(tree.val)

            # Traverse the left subtree first
            if not dfs(tree.left):
                return False
            # Then visit the current node
            nonlocal prev
            if tree.val <= prev:
                return False
            prev = tree.val
            # Finally traverse the right subtree
            return dfs(tree.right)

        for tree in trees:
            # Find the root of the merged tree
            if tree.val not in leaves:
                # Remove it from the hash map
                candidates.pop(tree.val)
                # Traverse from the root
                # A strictly increasing inorder traversal that visits every tree root forms a valid BST
                return tree if dfs(tree) and not candidates else None

        return None
