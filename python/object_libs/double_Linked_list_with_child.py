from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def list_to_double_linked_list(nums: list[Optional[int]]) -> Optional[Node]:
    if not nums:
        return None
    head = Node(nums[0], None, None, None)
    curr = head
    curr_head = head
    idx = 1
    while idx < len(nums):
        is_child = False
        if nums[idx] is None:
            curr = curr_head
            is_child = True
            idx += 1
        while nums[idx] is None:
            if curr:
                curr = curr.next
            idx += 1
        if is_child:
            curr.child = Node(nums[idx], None, None, None)
            curr = curr.child
            curr_head = curr
        else:
            curr.next = Node(nums[idx], curr, None, None)
            curr = curr.next
        idx += 1
    return head

def double_linked_list_to_list(head: Optional[Node]) -> list[Optional[int]]:
    ans = []
    curr_head, curr, nxt = head, head, None
    while curr or nxt:
        if not curr:
            curr = curr_head
            ans.append(None)
            while curr.child != nxt:
                curr = curr.next
                ans.append(None)
            curr = curr_head = nxt
            nxt = None
        if curr.child:
            nxt = curr.child
        ans.append(curr.val)
        curr = curr.next
    return ans
