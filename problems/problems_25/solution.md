# [Python] 模拟

> Author: Benhao
> Date: 2024-03-20
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [25. K 个一组翻转链表](https://leetcode.cn/problems/reverse-nodes-in-k-group/description/)

[TOC]

# 思路

> 先找到要处理的这一段，递归处理后面，再将这一段翻转，从头开始一个个链接到尾部

# 解题方法

> 模拟

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
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
  
