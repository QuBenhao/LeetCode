# [Python] Two priority queues: 100% in both metrics

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 5
> Tags: Python, Python3

---

### Approach
Order idle servers by `weight` and `index`, and busy servers by `finish time`, `weight`, and `index`.
Process the tasks in order.
Move busy servers that have finished by the task's arrival time into the idle queue.
If a server is idle, take the one with the smallest weight and move it into the busy queue.
Otherwise, take the earliest-finishing busy server with the smallest weight and reinsert it with its new finish time.

### Code

```python3
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []
        pq = []
        for i,s in enumerate(servers):
            heapq.heappush(pq, (s, i))
        use = []
        for base, task in enumerate(tasks):
            while use and use[0][0] <= base:
                _,s,i = heapq.heappop(use)
                heapq.heappush(pq, (s, i))
            if pq:
                s,i = heapq.heappop(pq)
                ans.append(i)
                heapq.heappush(use, (base+task, s, i))
            else:
                t, s, i = heapq.heappop(use)
                ans.append(i)
                heapq.heappush(use, (t + task, s, i))
        return ans
```
