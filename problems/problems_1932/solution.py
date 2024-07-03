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
        # 存储所有叶节点值的哈希集合
        leaves = set()
        # 存储 (根节点值, 树) 键值对的哈希映射
        candidates = dict()
        for tree in trees:
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
            candidates[tree.val] = tree

        # 存储中序遍历上一个遍历到的值，便于检查严格单调性
        prev = float("-inf")

        # 中序遍历，返回值表示是否有严格单调性
        def dfs(tree: Optional[TreeNode]) -> bool:
            if not tree:
                return True

            # 如果遍历到叶节点，并且存在可以合并的树，那么就进行合并
            if not tree.left and not tree.right and tree.val in candidates:
                tree.left = candidates[tree.val].left
                tree.right = candidates[tree.val].right
                # 合并完成后，将树丛哈希映射中移除，以便于在遍历结束后判断是否所有树都被遍历过
                candidates.pop(tree.val)

            # 先遍历左子树
            if not dfs(tree.left):
                return False
            # 再遍历当前节点
            nonlocal prev
            if tree.val <= prev:
                return False
            prev = tree.val
            # 最后遍历右子树
            return dfs(tree.right)

        for tree in trees:
            # 寻找合并完成后的树的根节点
            if tree.val not in leaves:
                # 将其从哈希映射中移除
                candidates.pop(tree.val)
                # 从根节点开始进行遍历
                # 如果中序遍历有严格单调性，并且所有树的根节点都被遍历到，说明可以构造二叉搜索树
                return tree if dfs(tree) and not candidates else None

        return None
