# [Python/Go] 链表模拟

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 6
> Tags: Go, Python, Python3

---

### 解题思路
将所有非0叠加到前面的0上，断开所有非0点，将最后一个0去掉即可

### 代码

```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end, last, cur = None, head, head.next
        while cur:
            if not cur.val:
                end,last = last,cur
            else:
                last.val += cur.val
                last.next = cur.next
            cur = cur.next
        end.next = None
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
func mergeNodes(head *ListNode) *ListNode {
    end, last, cur := head, head, head.Next
    for cur != nil {
        if cur.Val == 0 {
            end, last = last, cur
        } else {
            last.Val += cur.Val
            last.Next = cur.Next
        }
        cur = cur.Next
    }
    end.Next = nil
    return head
}
``` 