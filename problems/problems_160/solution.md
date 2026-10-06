# [Python] Long Time No See

> Author: Benhao
> Date: 2021-06-03
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
**我来到你的城市，走过你来时的路**

Imagine two people running at the same speed on tracks of different lengths.

If the tracks intersect, they must reach the same endpoint. (This also shows that checking whether the final nodes are identical can determine whether the lists intersect.)
The problem is that if their tracks have different lengths before the intersection, they reach both the intersection and the endpoint at different times.
Suppose you are a fair referee. You say, "That will not do. Why does one person run the inner track while the other runs the outer track? The inner-track runner must run the outer track too!",
The inner-track runner objects: "If I run the outer track now, does my earlier run on the inner track count for nothing?",
You think, "Fair point. To make this fair and transparent, the outer-track runner should also run the inner track!"
Now both people have run the same total distance. Since their distances are equal, they reach the endpoint at the same time, so they must also reach the intersection at the same time: the distance from the intersection to the endpoint is the same for both.

If the tracks do not intersect, the two people occupy different positions at every moment.

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
            return
        n1, n2 = headA, headB
        while n1 is not None or n2 is not None:
            if n1 == n2:
                return n1
            if n1 is None:
                n1 = headB
            else:
                n1 = n1.next
            if n2 is None:
                n2 = headA
            else:
                n2 = n2.next
```
