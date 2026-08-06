# [Python/Go] 长度遍历 / 快慢指针

> slug: pythongo-chang-du-bian-li-by-himymben-60ia
> date: 2021-12-05
> tags: Go, Python, Python3
> question: Delete the Middle Node of a Linked List (delete-the-middle-node-of-a-linked-list)
> url: https://leetcode.cn/problems/delete-the-middle-node-of-a-linked-list/solutions/O2IK9k/pythongo-chang-du-bian-li-by-himymben-60ia/

---
### 解题思路
特判一个节点的情况

or

快慢指针经典运用

### 代码

```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        l = 0
        while h:
            l += 1
            h = h.next
        if l == 1:
            return None
        h = head
        for i in range(l//2-1):
            h = h.next
        h.next = h.next.next
        return head
```
```Go []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    len := 0
    h := head
    for h != nil {
        len++
        h = h.Next
    }
    if len == 1{
        return nil
    }
    h = head
    for i := 0; i < len / 2 - 1; i++ {
        h = h.Next
    }
    h.Next = h.Next.Next
    return head
}
```

快慢指针
```python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = slow = fast = head
        while fast:
            fast = fast.next
            if not fast:
                break
            fast = fast.next
            pre = slow
            slow = slow.next
        if pre == slow:
            return None
        pre.next = pre.next.next
        return head
```
```Go []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    pre, slow, fast := head, head, head
    for fast != nil {
        fast = fast.Next
        if fast == nil {
            break
        }
        fast = fast.Next
        pre = slow
        slow = slow.Next
    }
    if pre == slow {
        return nil
    }
    pre.Next = pre.Next.Next
    return head
}
```