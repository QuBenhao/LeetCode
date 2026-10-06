# [Python] Iterative solution without a dummy head

> Author: Benhao
> Date: 2021-03-25
> Upvotes: 2
> Tags: Python

---

### Approach
If head.next has the same value as head, keep advancing until a value differs from head. **The list is sorted.**
If the values differ, keep head and look for the next head starting from head.next.

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
        if front and front.val == head.val:
            while front and front.val == head.val:
                front = front.next
            return self.deleteDuplicates(front)
        head.next = self.deleteDuplicates(front) 
        return head

```
