import solution
from python.object_libs import tree_next_node_to_list, list_to_tree_next_node


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree_next_node(test_input)
        node = self.connect(root)
        return tree_next_node_to_list(node)

    def connect(self, root: Node) -> Node:
        if not root:
            return root
        head = root
        while head:
            cur = head
            child_head = child_last = None
            while cur:
                if cur.left:
                    if not child_head:
                        child_head = cur.left
                    if not child_last:
                        child_last = cur.left
                    else:
                        child_last.next = cur.left
                        child_last = child_last.next
                if cur.right:
                    if not child_head:
                        child_head = cur.right
                    if not child_last:
                        child_last = cur.right
                    else:
                        child_last.next = cur.right
                        child_last = child_last.next
                cur = cur.next
            head = child_head
        return root
