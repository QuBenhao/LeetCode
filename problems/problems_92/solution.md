# [Python] 不停迭代直到变为left是头的情况，再到left==right

> Author: Benhao
> Date: 2021-03-17
> Upvotes: 1
> Tags: Python

---

### 解题思路
当head不在left和right中，迭代统计left和right的位置
当head是left以后，统计right的位置，记录right.next为successor，从后往前依次反转链表

front -> 1 -> 2 -> 3 -> 4 -> successor

front -> 1 -> 2 (2 __> 3)   4 -> 3 -> successor

front -> 1 (1__>2) 4 -> 3 -> 2 -> successor

front -> 4 -> 3 -> 2 -> 1 ->successor

### 代码

```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next
        for _ in range(right - left):
            next_node = cur.next
            cur.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        return dummy.next
```
```python3 []
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == 1:
            if right == 1:
                self.successor = head.next
                return head
            final = self.reverseBetween(head.next, left, right - 1)
            head.next.next = head
            head.next = self.successor
            return final
        
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

```
