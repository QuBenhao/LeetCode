# [Python] Fast and slow pointers

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/description/)

[TOC]

# Intuition

> If a cycle exists, the faster traveler must eventually catch the slower one.

# Approach

> Move the fast pointer two steps and the slow pointer one step at a time. If the fast pointer catches the slow pointer, a cycle exists. Otherwise, it reaches the end of the list and the process stops.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
> $O(1)$



# Code
```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast:
            if fast.next:
                fast = fast.next.next
            else:
                break
            slow = slow.next
            if fast == slow:
                return True
        return False
```
  
