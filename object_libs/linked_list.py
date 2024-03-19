from collections import deque
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(nums: list[int]) -> Optional[ListNode]:
    if not nums:
        return
    dq = deque(nums)
    head = ListNode(dq.popleft())
    curr = head
    while dq:
        curr.next = ListNode(dq.popleft())
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result
