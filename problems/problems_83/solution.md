# [Python] 依旧是迭代

> Author: Benhao
> Date: 2021-03-25
> Upvotes: 1
> Tags: Python

---

### 解题思路
有重复就让head.next=后面的部分即可

### 代码

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