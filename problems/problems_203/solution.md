# [Python] Simplify with a dummy node

> Author: Benhao
> Date: 2021-06-04
> Upvotes: 4
> Tags: Python, Python3

---

### Approach
Traverse with a current pointer and a previous pointer. If the current node should be deleted, set the previous node's next to the current node's next; otherwise, advance both pointers normally.

**Also**
Problems involving node removal from linked lists can generally be solved either iteratively or recursively.
If the current node should be deleted, return its next node as the new head. Otherwise, process the remainder of the list and return the current node as the unchanged head.
```python3
        if not head:
            return head
        # Process the remainder of the list
        head.next = self.removeElements(head.next, val)
        # Determine the head
        return head.next if head.val == val else head
```

### Code

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0,head)
        node, last = head, dummy
        while node:
            if node.val == val:
                last.next = node.next
            else:
                last = last.next
            node = node.next
        return dummy.next

```
