import solution
from python.object_libs import list_to_linked_random_list, linked_random_list_to_list


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(solution.Solution):
    def solve(self, test_input=None):
        head = list_to_linked_random_list(test_input)
        return linked_random_list_to_list(self.copyRandomList(head))

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # Copy every node and insert the copy after the original node
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next, None)
            cur = cur.next.next

        # Connect the random pointers of all copied nodes
        cur = head
        copy_head = head.next
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # Disconnect the original list from the copied list
        cur = head
        cur_ = copy_head
        while cur and cur_:
            cur.next = cur_.next
            cur = cur.next
            if cur:
                cur_.next = cur.next
            cur_ = cur_.next
        return copy_head
