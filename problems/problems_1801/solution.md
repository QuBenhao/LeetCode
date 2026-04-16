# [Python] 优先队列

> Author: Benhao
> Date: 2021-03-21
> Upvotes: 0
> Tags: Python

---

### 解题思路
sells按从小到大,buys按从大到小。所以buy中用-price

### 代码

```python
class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        import heapq
        sells = []
        buys = []
        for p,a,t in orders:
            if t == 0:
                while sells:
                    p_, a_ = heapq.heappop(sells)
                    if p_ <= p:
                        if a >= a_:
                            a -= a_
                        else:
                            heapq.heappush(sells, (p_, a_-a))
                            a = 0
                            break
                    else:
                        heapq.heappush(sells, (p_, a_))
                        break
                if a:
                    heapq.heappush(buys, (-p, a))
            else:
                while buys:
                    p_, a_ = heapq.heappop(buys)
                    p_ = -p_
                    if p_ >= p:
                        if a >= a_:
                            a -= a_
                        else:
                            heapq.heappush(buys, (-p_, a_-a))
                            a = 0
                            break
                    else:
                        heapq.heappush(buys, (-p_, a_))
                        break
                if a:
                    heapq.heappush(sells, (p, a))
        return (sum(x[1] for x in sells) + sum(x[1] for x in buys)) % (10**9+7)
```