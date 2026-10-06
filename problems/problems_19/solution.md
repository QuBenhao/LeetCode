# [Python] Fast and slow pointers

> Author: Benhao
> Date: 2024-04-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

[TOC]

# Intuition

> To find the nth node from the end, move the fast pointer n steps ahead of the slow pointer. When the fast pointer reaches the end, the slow pointer is at the desired node.

# Approach

> Fast and slow pointers

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = dummy_head = ListNode(next=head)
        fast = head
        while fast and n:
            fast = fast.next
            n -= 1
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
```
  
