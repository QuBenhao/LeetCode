# [Python] 左右指针，取余数

> Author: Benhao
> Date: 2021-03-27
> Upvotes: 1
> Tags: Python

---

### 解题思路
当k比链表长度小的时候，
从head出发往右k次，这样左右指针的差距就是k了。
左右一起挪，右边挪到底的时候，左边就是新的头了，重新连一下即可。

当k比链表长度大的时候，需要取余数，相当于套圈。
（我们从head出发往右，到达最后一个了，k却没到0，我们也能从我们减了多少求得链表的长度）

### 代码

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head
        right = head
        temp = k
        while right.next and k:
            right = right.next
            k -= 1
        if k:
            k -= 1
            k %= temp - k
            return self.rotateRight(head, k)

        left = head
        while right.next:
            left = left.next
            right = right.next

        right.next = head
        head = left.next
        left.next = None

        return head

```