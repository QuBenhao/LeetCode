# [Python] 快慢指针

> Author: Benhao
> Date: 2024-04-03
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [19. 删除链表的倒数第 N 个结点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/)

[TOC]

# 思路

> 要找到倒数第n个，只要快指针比慢指针先走n步，这样快指针到结尾的时候慢指针就是我们想要到节点

# 解题方法

> 快慢指针

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
