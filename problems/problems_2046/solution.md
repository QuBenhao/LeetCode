# [Python] 模拟

> slug: python-by-himymben-jfpf
> date: 2022-05-02
> tags: Python, Python3
> question: Sort Linked List Already Sorted Using Absolute Values (sort-linked-list-already-sorted-using-absolute-values)
> url: https://leetcode.cn/problems/sort-linked-list-already-sorted-using-absolute-values/solutions/q5EQzx/python-by-himymben-jfpf/

---
### 解题思路
因为已经按绝对值排好序，所以每次遇到正数不变，遇到负数将负数断开后拼接到头即可

### 代码

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