from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(nums: list[Optional[int]]) -> Optional[TreeNode]:
    if not nums:
        return
    root = TreeNode(nums[0])
    is_left = 1
    curr_nodes = deque([])
    curr_node = root
    for i in range(1, len(nums)):
        num = nums[i]
        if is_left:
            if num is not None:
                curr_node.left = TreeNode(val=num)
                curr_nodes.append(curr_node.left)
        else:
            if num is not None:
                curr_node.right = TreeNode(val=num)
                curr_nodes.append(curr_node.right)
            curr_node = curr_nodes.popleft()
        is_left ^= 1
    return root


def list_to_tree_with_target(nums: list[Optional[int]], *args) -> tuple[Optional[TreeNode], ...]:
    if not nums:
        return None, *[None] * len(args)
    root = TreeNode(nums[0])
    target_nodes = [None for _ in range(len(args))]
    for i, target in enumerate(args):
        if nums[0] == target:
            target_nodes[i] = root
    is_left = 1
    curr_nodes = deque([])
    curr_node = root
    for i in range(1, len(nums)):
        num = nums[i]
        if is_left:
            if num is not None:
                curr_node.left = TreeNode(val=num)
                for i, target in enumerate(args):
                    if num == target:
                        target_nodes[i] = curr_node.left
                curr_nodes.append(curr_node.left)
        else:
            if num is not None:
                curr_node.right = TreeNode(val=num)
                for i, target in enumerate(args):
                    if num == target:
                        target_nodes[i] = curr_node.right
                curr_nodes.append(curr_node.right)
            curr_node = curr_nodes.popleft()
        is_left ^= 1
    return root, *target_nodes


def tree_to_list(root: Optional[TreeNode]) -> list[Optional[int]]:
    ans = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        ans.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while ans and ans[-1] is None:
        ans.pop()
    return ans
