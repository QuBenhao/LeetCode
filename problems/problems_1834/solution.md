# [Python] 优先队列

> Author: Benhao
> Date: 2021-04-18
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
任务按(开始时间，时长，下标)从大到小排序。
如果当前队列有任务，执行任务，更新时间；如果没有，从任务表中出任务，更新时间。
根据时间将任务压入队列中，按（时长，下标，开始时间）入队，这里开始时间其实只是为了更新时间用。

### 代码

```python3
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted(enumerate(tasks), key=lambda x: (-x[1][0],-x[1][1],-x[0]))
        ans = []
        pq = []
        time = 0
        while tasks or pq:
            if pq:
                l, idx, t = heapq.heappop(pq)
            else:
                idx, v = tasks.pop()
                t, l = v
            ans.append(idx)
            time = max(t,time) + l
            while tasks and tasks[-1][1][0] <= time:
                index, val = tasks.pop()
                ti, le = val
                heapq.heappush(pq, (le, index, ti))
        return ans
```