# [Python] 好久不见

> Author: Benhao
> Date: 2021-06-03
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
**我来到你的城市，走过你来时的路**

考虑有两个人以同样的速度在两个不一样长的跑道上跑步。

如果相交，那么他们必然会到达同样的终点(也可以看出，本质上通过判断末尾节点是否相同来判断有没有相交)。
问题是，如果他们之前的跑道长短不一，他们到达终点以及相交点的时间都是不一样的。
假设你是个公正的裁判，这时候你说:"那不行啊，凭什么一个跑内圈，另一个跑外圈？跑内圈的也得去跑外圈去！",
这时候跑内圈的又不干了，他说:"不是我再跑个外圈我之前跑的内圈就白跑了？",
这时候你想:"也对，那为了公平公正公开，跑外圈的人再跑一下内圈吧！"
于是两个人终于跑了同样的路，因为长度一致了，俩人是同时到终点，那么俩人肯定也是同时到的交点（因为交点到终点的长度俩人都一样）。

如果不相交，那么两个人每个时刻所在的位置都是不一样的。

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