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


def list_to_linked_list_intersection(iv: int, nums1: list[int], nums2: list[int], idx1: int, idx2: int) -> list[Optional[ListNode]]:
    if iv == 0:
        return [list_to_linked_list(nums1), list_to_linked_list(nums2)]
    head1, head2 = ListNode(nums1[0]), ListNode(nums2[0]) if idx2 > 0 else None
    node1 = head1
    for i in range(1, idx1 + 1):
        node1.next = ListNode(nums1[i])
        node1 = node1.next
    if idx2 == 0:
        head2 = node1
    else:
        node2 = head2
        for i in range(1, idx2):
            node2.next = ListNode(nums2[i])
            node2 = node2.next
        node2.next = node1
    for i in range(idx1 + 1,  len(nums1)):
        node1.next = ListNode(nums1[i])
        node1 = node1.next
    return [head1, head2]


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result
