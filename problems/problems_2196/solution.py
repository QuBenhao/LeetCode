import solution
from typing import *
from python.object_libs import tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        descriptions = test_input
        res = self.createBinaryTree(descriptions)
        return tree_to_list(res)

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        # 哈希表存储节点值到节点的映射
        nodes = {}
        # 记录所有子节点，用于找根节点
        children = set()

        for parent_val, child_val, is_left in descriptions:
            # 确保父节点存在
            if parent_val not in nodes:
                nodes[parent_val] = TreeNode(parent_val)
            # 确保子节点存在
            if child_val not in nodes:
                nodes[child_val] = TreeNode(child_val)

            # 建立父子关系
            if is_left:
                nodes[parent_val].left = nodes[child_val]
            else:
                nodes[parent_val].right = nodes[child_val]

            # 记录子节点
            children.add(child_val)

        # 根节点 = 不在 children 集合中的节点
        for val in nodes:
            if val not in children:
                return nodes[val]

        return None

