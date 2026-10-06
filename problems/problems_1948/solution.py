import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deleteDuplicateFolder(test_input)

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = TrieNode()
        for path in paths:
            # Insert path into the trie; see 208. Implement Trie
            cur = root
            for s in path:
                if s not in cur.son:
                    cur.son[s] = TrieNode()
                cur = cur.son[s]
                cur.name = s

        expr_to_node = {}  # Parenthesized subtree expression -> subtree root

        def gen_expr(node: TrieNode) -> str:
            if not node.son:  # Leaf
                return node.name  # The expression is just the folder name

            # Wrap each subtree expression in parentheses
            expr = sorted('(' + gen_expr(son) + ')' for son in node.son.values())
            sub_tree_expr = ''.join(expr)  # Concatenate all subtree expressions in lexicographic order
            if sub_tree_expr in expr_to_node:  # An existing sub_tree_expr in the map indicates duplicate folders
                expr_to_node[sub_tree_expr].deleted = True  # Mark the node recorded in the map for deletion
                node.deleted = True  # Mark the current node for deletion
            else:
                expr_to_node[sub_tree_expr] = node

            return node.name + sub_tree_expr

        for son in root.son.values():
            gen_expr(son)

        ans = []
        path = []

        # Backtrack through the trie, visiting only undeleted nodes and recording their paths in the answer
        # Similar to 257. Binary Tree Paths
        def dfs(node: TrieNode) -> None:
            if node.deleted:
                return
            path.append(node.name)
            ans.append(path.copy())  # path[:]
            for child in node.son.values():
                dfs(child)
            path.pop()  # Restore the previous state

        for son in root.son.values():
            dfs(son)

        return ans

class TrieNode:
    __slots__ = 'son', 'name', 'deleted'

    def __init__(self):
        self.son = {}
        self.name = ''  # Folder name
        self.deleted = False  # Deletion flag
