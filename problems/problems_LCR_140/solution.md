# [Python/Java] Fast and slow pointers

> slug: pythonjava-kuai-man-zhi-zhen-by-himymben-3v9x
> date: 2021-09-01
> tags: Java, Python, Python3
> question: 训练计划 II (lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof)
> url: https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solutions/UKJ8va/pythonjava-kuai-man-zhi-zhen-by-himymben-3v9x/

---
### Approach
Keep the fast pointer k nodes ahead of the slow pointer. When the fast pointer reaches the end, the slow pointer is at the desired node.

### Code

```Python3 []
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head
        while k:
            fast = fast.next
            k -= 1
        while fast:
            slow = slow.next
            fast = fast.next
        return slow
```
```Java []
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode slow = head, fast = head;
        for(int i=0;i<k;i++)
            fast = fast.next;
        while(fast!=null){
            slow = slow.next;
            fast = fast.next;
        }
        return slow;
    }
}
```
