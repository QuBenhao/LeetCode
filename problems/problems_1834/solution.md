# [Python] Priority queue

> Author: Benhao
> Date: 2021-04-18
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Sort tasks in descending order by (start time, duration, index).
If the queue has a task, execute it and update the time. Otherwise, take one from the task list and update the time.
Enqueue tasks as they become available using (duration, index, start time). The start time is needed only for updating the clock.

### Code

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
