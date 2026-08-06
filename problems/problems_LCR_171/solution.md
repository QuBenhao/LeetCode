# [Python/Java] 相遇问题

> slug: python-xiang-yu-wen-ti-by-qubenhao-jhm5
> date: 2021-07-20
> tags: Java, Python, Python3
> question: 训练计划 V (liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof)
> url: https://leetcode.cn/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solutions/Z6eM1E/python-xiang-yu-wen-ti-by-qubenhao-jhm5/

---
### 解题思路
两个节点分别从headA, headB出发，到达终点时交换起点，这样他们到达交点走过的节点数就一致了(同时到达交点)。

没有交点的情况，A和B最终会一起变成None。

### 代码

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