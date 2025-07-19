import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deleteDuplicateFolder(test_input)

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in paths:
            # 把 path 插到字典树中，见 208. 实现 Trie
            cur = root
            for s in path:
                if s not in cur.son:
                    cur.son[s] = TrieNode()
                cur = cur.son[s]
                cur.name = s

        expr_to_node = {}  # 子树括号表达式 -> 子树根节点

        def gen_expr(node: TrieNode) -> str:
            if not node.son:  # 叶子
                return node.name  # 表达式就是文件夹名

            # 每个子树的表达式外面套一层括号
            expr = sorted('(' + gen_expr(son) + ')' for son in node.son.values())
            sub_tree_expr = ''.join(expr)  # 按字典序拼接所有子树的表达式
            if sub_tree_expr in expr_to_node:  # 哈希表中有 sub_tree_expr，说明有重复的文件夹
                expr_to_node[sub_tree_expr].deleted = True  # 哈希表中记录的节点标记为删除
                node.deleted = True  # 当前节点标记为删除
            else:
                expr_to_node[sub_tree_expr] = node

            return node.name + sub_tree_expr

        for son in root.son.values():
            gen_expr(son)

        ans = []
        path = []

        # 在字典树上回溯，仅访问未被删除的节点，并将路径记录到答案中
        # 类似 257. 二叉树的所有路径
        def dfs(node: TrieNode) -> None:
            if node.deleted:
                return
            path.append(node.name)
            ans.append(path.copy())  # path[:]
            for child in node.son.values():
                dfs(child)
            path.pop()  # 恢复现场

        for son in root.son.values():
            dfs(son)

        return ans

class TrieNode:
    __slots__ = 'son', 'name', 'deleted'

    def __init__(self):
        self.son = {}
        self.name = ''  # 文件夹名称
        self.deleted = False  # 删除标记
