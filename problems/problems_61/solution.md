# [Python] Left and right pointers with modulo

> Author: Benhao
> Date: 2021-03-27
> Upvotes: 1
> Tags: Python

---

### Approach
When k is smaller than the list length,
move right from head k times, leaving a gap of k between the left and right pointers.
Move both pointers together. When the right pointer reaches the end, the left pointer is the new head; reconnect the list.

When k is greater than the list length, take the remainder, which accounts for full laps.
(If we move right from head and reach the last node before k reaches 0, the amount subtracted also tells us the list length.)

### Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        right = head
        temp = k
        while right.next and k:
            right = right.next
            k -= 1
        if k:
            k -= 1
            k %= temp - k
            return self.rotateRight(head, k)

        left = head
        while right.next:
            left = left.next
            right = right.next

        right.next = head
        head = left.next
        left.next = None

        return head

```
