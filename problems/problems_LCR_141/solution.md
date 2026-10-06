# [Python] Reverse a linked list

> slug: python-fan-zhuan-lian-biao-by-himymben-u0ru
> date: 2022-03-26
> tags: Python, Python3
> question: 训练计划 III (fan-zhuan-lian-biao-lcof)
> url: https://leetcode.cn/problems/fan-zhuan-lian-biao-lcof/solutions/iWMB4X/python-fan-zhuan-lian-biao-by-himymben-u0ru/

---
### Approach
Reverse the list in place.

### Code

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

```
