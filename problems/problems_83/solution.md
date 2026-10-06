# [Python] Iteration again

> Author: Benhao
> Date: 2021-03-25
> Upvotes: 1
> Tags: Python

---

### Approach
When a duplicate occurs, set head.next to the remaining portion of the list.

### Code

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        front = head.next
        while front and front.val == head.val:
            front = front.next
        head.next = self.deleteDuplicates(front)
        return head

```
