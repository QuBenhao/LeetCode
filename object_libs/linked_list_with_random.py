from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


def list_to_linked_random_list(arr: list[list[Optional[int]]]) -> Optional[Node]:
    n = len(arr)
    if not n:
        return
    node_list = [Node(0) for _ in range(n)]
    for i, (val, idx) in enumerate(arr):
        node = node_list[i]
        node.val = val
        if i < n - 1:
            node.next = node_list[i + 1]
        if idx is not None:
            node.random = node_list[idx]
    return node_list[0]


def linked_random_list_to_list(head: Optional[Node]) -> list[list[Optional[int]]]:
    ans = []
    idx_map = dict()
    node, i = head, 0
    while node:
        idx_map[node] = i
        node = node.next
        i += 1
    node = head
    while node:
        ans.append([node.val, idx_map.get(node.random, None)])
        node = node.next
    return ans
