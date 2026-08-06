# [Python/Java] 快慢指针

> slug: pythonjava-kuai-man-zhi-zhen-by-himymben-3v9x
> date: 2021-09-01
> tags: Java, Python, Python3
> question: 训练计划 II (lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof)
> url: https://leetcode.cn/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solutions/UKJ8va/pythonjava-kuai-man-zhi-zhen-by-himymben-3v9x/

---
### 解题思路
快指针比慢指针快k个结点，这样当快指针到结尾的时候，慢指针就是我们想要的了。

### 代码

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