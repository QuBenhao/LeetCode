# [Python] 最小堆

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 5
> Tags: Python, Python3

---

### 解题思路
按占椅子发生的时间顺序排序；
按时间维护一个被占用的椅子，再维护一个当前时间没被占用的椅子们即可

### 代码

```python3
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        times = sorted(enumerate(times), key=lambda x:(x[1][0],x[0],-x[1][1]))
        curr = []
        avl = [i for i in range(n)]
        for i, (arr, leave) in times:
            while curr and curr[0][0] <= arr:
                _,idx = heapq.heappop(curr)
                heapq.heappush(avl, idx)
            c = heapq.heappop(avl)
            if i == targetFriend:
                return c
            heapq.heappush(curr, (leave, c))
        return -1
```