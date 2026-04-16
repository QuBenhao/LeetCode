# [Python] 快慢指针

> Author: Benhao
> Date: 2021-07-28
> Upvotes: 1
> Tags: Java, Python, Python3

---

### 解题思路
首先，有环快慢指针必然会相遇。而且他们相遇的话，慢指针刚进入环的入口的时候，快指针必然领先了慢指针`x%C`的长度，那么快指针要追上慢指针就要走`-x%C`。他们相遇的时候相当于慢指针走了`-x%C`。这个时候从头走到入口和从这个相遇的位置走到入口距离是一致的。我们再从头出发一个相遇即可。

### 代码
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
