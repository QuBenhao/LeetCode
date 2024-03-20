from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(nums: list[int]) -> Optional[ListNode]:
    if not nums:
        return
    head = ListNode(nums[0])
    curr = head
    for i in range(1, len(nums)):
        curr.next = ListNode(nums[i])
        curr = curr.next
    return head


def list_to_linked_list_cycle(nums: list[int], pos) -> Optional[ListNode]:
    if not nums or pos == -1:
        return list_to_linked_list(nums)
    n = len(nums)
    last = node = ListNode(nums[-1])
    if pos == n - 1:
        last.next = last
    for i in range(n - 2, -1, -1):
        node = ListNode(nums[i], node)
        if i == pos:
            last.next = node
    return node


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result
