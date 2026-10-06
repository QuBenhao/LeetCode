import solution
from typing import *
from python.object_libs import list_to_linked_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        head0 = list_to_linked_list(nums0)
        return self.pairSum(head0)

    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. Find the midpoint with fast and slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half of the linked list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # prev is the head of the reversed second half

        # 3. Traverse the first half and reversed second half together to compute the maximum twin sum
        max_sum = 0
        first, second = head, prev
        while second:
            cur_sum = first.val + second.val
            if cur_sum > max_sum:
                max_sum = cur_sum
            first = first.next
            second = second.next

        return max_sum

