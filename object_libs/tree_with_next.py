from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def list_to_tree_next_node(nums: list[Optional[int]]) -> Optional[Node]:
    if not nums:
        return
    root = Node(nums[0])
    is_left = 1
    curr_nodes = deque([])
    curr_node = root
    for i in range(1, len(nums)):
        num = nums[i]
        if is_left:
            if num is not None:
                curr_node.left = Node(val=num)
                curr_nodes.append(curr_node.left)
        else:
            if num is not None:
                curr_node.right = Node(val=num)
                curr_nodes.append(curr_node.right)
            curr_node = curr_nodes.popleft()
        is_left ^= 1
    return root


def tree_next_node_to_list(node: Optional[Node]) -> list[int]:
    result = []
    if not node:
        return result
    head = node
    while head:
        nxt_head = None
        cur = head
        while cur:
            nxt_head = nxt_head or cur.left or cur.right
            result.append(cur.val)
            cur = cur.next
        result.append(None)
        head = nxt_head
    return result
