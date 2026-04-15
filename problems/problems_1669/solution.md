# [Python] 直接重连

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
找到各处连接点

### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if a == list1.val:
            root = list2
        else:
            root = list1
        l1 = list1
        node = list2
        count = 1
        while count < a:
            l1 = l1.next
            count += 1
        r1 = l1
        while count <= b:
            r1 = r1.next
            count += 1
        r1 = r1.next
        while node.next is not None:
            node = node.next
        l1.next = list2
        node.next = r1
        return root
```