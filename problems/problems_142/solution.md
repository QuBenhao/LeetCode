# [Python] Fast and slow pointers

> Author: Benhao
> Date: 2021-07-28
> Upvotes: 1
> Tags: Java, Python, Python3

---

### Approach
First, if a cycle exists, the fast and slow pointers must meet. When the slow pointer first enters the cycle, the fast pointer is ahead by `x%C`, so catching the slow pointer requires covering `-x%C`. By the time they meet, the slow pointer has traveled `-x%C` within the cycle. The distance from the head to the cycle entry is then the same as the distance from the meeting point to the entry. Start another pointer from the head and let the two pointers meet again.

### Code
```python3 []
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return
        fast = slow = head
        while fast:
            if not fast.next:
                return
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast:
            return
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
```
```java []
public class Solution {
    public ListNode detectCycle(ListNode head) {
        if(head==null) return null;
        ListNode fast = head, slow = head;
        while(fast != null){
            if(fast.next==null)
                return null;
            fast = fast.next.next;
            slow = slow.next;
            if(fast==slow)
                break;
        }
        if(fast == null) return null;
        fast = head;
        while(fast != slow){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
```
