# [Python] 使用dummy偷个懒

> Author: Benhao
> Date: 2021-06-04
> Upvotes: 4
> Tags: Python, Python3

---

### 解题思路
每次遍历当前指针和前一个指针，如果当前指针的值要删除，就将前一个指针的next变成当前的next即可；否则两者正常往后移。

**另外**
一般这种移除链表节点的题都可以使用迭代or递归来解决。
比如说如果当前节点是要删除的点，那么返回的就是它的next(作为新的头)；否则处理后面的部分然后返回自己作为头（头不变）；
```python3
        if not head:
            return head
        # 处理后面的部分
        head.next = self.removeElements(head.next, val)
        # 谁是头
        return head.next if head.val == val else head
```

### 代码

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0,head)
        node, last = head, dummy
        while node:
            if node.val == val:
                last.next = node.next
            else:
                last = last.next
            node = node.next
        return dummy.next

```