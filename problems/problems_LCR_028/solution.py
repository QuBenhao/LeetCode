import solution
from typing import *
from python.object_libs import list_to_double_linked_list, double_linked_list_to_list



# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_double_linked_list(test_input)
        return double_linked_list_to_list(self.flatten(head))

    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node: 'Node') -> Optional['Node']:
            if not node:
                return None
            tail = curr = node
            while curr:
                if curr.child:
                    tail_child = dfs(curr.child)
                    tail_child.next = curr.next
                    if curr.next:
                        curr.next.prev = tail_child
                    curr.next = curr.child
                    curr.child.prev = curr
                    curr.child = None
                    curr = tail_child.next
                    tail = tail_child
                else:
                    tail = curr
                    curr = curr.next
            return tail

        dfs(head)
        return head
