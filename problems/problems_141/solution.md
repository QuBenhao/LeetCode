# [Python] 快慢指针

> Author: Benhao
> Date: 2024-03-01
> Upvotes: 4
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [141. 环形链表](https://leetcode.cn/problems/linked-list-cycle/description/)

[TOC]

# 思路

> 如果存在环路，走的快的人一定能追上走的慢的人

# 解题方法

> 快指针每次移动两步，慢指针每次移动一步，如果快指针能追上慢指针，代表有环，否则会到链表末尾即结束

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
