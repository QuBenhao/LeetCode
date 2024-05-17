from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def list_relation_to_node_neigh(lst: list[list[int]]) -> Optional[Node]:
    if not lst:
        return None

    nodes = {}
    for i in range(1, len(lst) + 1):
        node = Node(i)
        nodes[i] = node

    for i, vals in enumerate(lst):
        nodes[i + 1].neighbors.extend([nodes[val] for val in vals])

    return nodes[1]


def node_neigh_to_list_relation(node: Optional[Node]) -> list[list[int]]:
    ans = []
    if not node:
        return ans

    explored = {1}

    def dfs(cur: Node):
        if len(ans) < cur.val:
            for i in range(len(ans), cur.val - 1):
                ans.append(None)
            ans.append([nd.val for nd in cur.neighbors])
        else:
            ans[cur.val - 1] = [nd.val for nd in cur.neighbors]
        for nd in cur.neighbors:
            if nd.val not in explored:
                explored.add(nd.val)
                dfs(nd)

    dfs(node)
    return ans
