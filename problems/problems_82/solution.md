# [Python] 迭代解法 不需要dummy head

> Author: Benhao
> Date: 2021-03-25
> Upvotes: 2
> Tags: Python

---

### 解题思路
如果head.next的值和head的值相等，那么我们要一直往前找，直到值和head的值不相等位置。**因为是排序链表**
如果不相等，说明head要被留下，那么转而寻找head.next后面的head。

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
        if front and front.val == head.val:
            while front and front.val == head.val:
                front = front.next
            return self.deleteDuplicates(front)
        head.next = self.deleteDuplicates(front) 
        return head

```