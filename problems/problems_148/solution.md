# [Python] 归并排序

> Author: Benhao
> Date: 2024-03-11
> Upvotes: 3
> Tags: Go, Java, Python3

---


> Problem: [148. 排序链表](https://leetcode.cn/problems/sort-list/description/)

[TOC]

# 思路

> 归并

# 解题方法

> 拆分链表，分别多两个子链表递归排序，最后再对多个有序进行归并


# Code
```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # cut
        mid = slow.next
        slow.next = None
        # sort each
        left, right = self.sortList(head), self.sortList(mid)
        # merge
        node = dummy = ListNode()
        while left and right:
            if left.val < right.val:
                node.next = ListNode(left.val)
                left = left.next
            else:
                node.next = ListNode(right.val)
                right = right.next
            node = node.next
        node.next = left if left else right
        return dummy.next
```
  
