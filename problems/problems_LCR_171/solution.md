# [Python/Java] Meeting pointers

> slug: python-xiang-yu-wen-ti-by-qubenhao-jhm5
> date: 2021-07-20
> tags: Java, Python, Python3
> question: 训练计划 V (liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof)
> url: https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solutions/Z6eM1E/python-xiang-yu-wen-ti-by-qubenhao-jhm5/

---
### Approach
Start two pointers at headA and headB, and switch each to the other head when it reaches the end. Both then travel the same number of nodes before reaching the intersection, so they arrive together.

If there is no intersection, A and B eventually become None at the same time.

### Code

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        A, B = headA, headB
        while A != B:
            if A is None:
                A = headB
            else:
                A = A.next
            if B is None:
                B = headA
            else:
                B = B.next
        return A
```

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null)
            return null;
        ListNode a = headA, b = headB;
        while(a != b){
            if(a  == null)
                a = headB;
            else
                a = a.next;
            if(b == null)
                b = headA;
            else
                b = b.next;
        }
        return a;
    }
}
```
