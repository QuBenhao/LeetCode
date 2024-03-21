import solution
from typing import *
from object_libs import list_relation_to_node_neigh, node_neigh_to_list_relation


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(solution.Solution):
    def solve(self, test_input=None):
        node = list_relation_to_node_neigh(test_input)
        return node_neigh_to_list_relation(self.cloneGraph(node))

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        explored = {}

        def dfs(nd: Node, neigh_clone: Optional[Node]):
            clone_nd = Node(nd.val)
            explored[nd.val] = clone_nd
            if neigh_clone:
                neigh_clone.neighbors.append(clone_nd)
            for neighbor in nd.neighbors:
                if neighbor.val in explored:
                    clone_nd.neighbors.append(explored[neighbor.val])
                else:
                    dfs(neighbor, clone_nd)

        dfs(node, None)

        return explored[node.val]
