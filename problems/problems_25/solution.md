# [Python] Simulation

> Author: Benhao
> Date: 2024-03-20
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/description/)

[TOC]

# Intuition

> First identify the segment to process, recursively process the rest, then reverse this segment by attaching its nodes to the tail one at a time from the head.

# Approach

> Simulation

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(n)$



# Code
```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        node = head
        for _ in range(k - 1):
            if not node:
                break
            node = node.next
        if not node:
            return head
        node.next = self.reverseKGroup(node.next, k)
        last = tail = node.next
        while head != last:
            nxt = head.next
            head.next = tail
            tail = head
            head = nxt
        return node
```
  
