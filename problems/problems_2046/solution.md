# [Python] Simulation

> slug: python-by-himymben-jfpf
> date: 2022-05-02
> tags: Python, Python3
> question: Sort Linked List Already Sorted Using Absolute Values (sort-linked-list-already-sorted-using-absolute-values)
> url: https://leetcode.cn/problems/sort-linked-list-already-sorted-using-absolute-values/solutions/q5EQzx/python-by-himymben-jfpf/

---
### Approach
The list is already sorted by absolute value. Leave positive values in place, and detach each negative value and prepend it to the head.

### Code

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = head, head.next
        while cur:
            if cur.val < 0:
                tmp = cur.next
                pre.next = tmp
                cur.next = head
                head = cur
                cur = tmp
            else:
                pre, cur = cur, cur.next
        return head 

```
