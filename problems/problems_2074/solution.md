# [Python] 92题反转链表 + 长度判断

> slug: python-92ti-fan-zhuan-lian-biao-chang-du-53zx
> date: 2021-11-14
> tags: Python, Python3
> question: Reverse Nodes in Even Length Groups (reverse-nodes-in-even-length-groups)
> url: https://leetcode.cn/problems/reverse-nodes-in-even-length-groups/solutions/49sJZX/python-92ti-fan-zhuan-lian-biao-chang-du-53zx/

---
```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(h, l):
            i,p, cur = 0, None, h
            # 检测剩余长度是否足够
            while i < l and cur:
                p = cur
                cur = cur.next
                i += 1
            if i % 2 != 0:
                return h, p
            # 设置 dummyNode 是这一类问题的一般做法
            dummy_node = ListNode(-1)
            dummy_node.next = h
            pre = dummy_node

            cur = pre.next
            for _ in range(i - 1):
                nt = cur.next
                cur.next = nt.next
                nt.next = pre.next
                pre.next = nt
            return dummy_node.next, h
        
        prev, node = None, head
        cur = 1
        while node:
            if prev:
                prev.next, node = reverseList(node, cur)
            prev = node
            node = node.next
            cur += 1
        return head

```