# [Python] 两个优先队列 双100%

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 5
> Tags: Python, Python3

---

### 解题思路
空闲服务器根据`权重`和`坐标`排序，使用中的服务器根据`结束时间`，`权重`和`坐标`排序。
遍历任务。
当我们有使用中的小于任务基础时间的服务器，将它们加入空闲（因为实际上任务已结束），
如果我们有空闲的服务器，在空闲队列中找权重最小的加入使用的队列中。
如果我们没有空闲的服务器，在使用队列中找最早完成且权重最小的，重新加入队列。

### 代码

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