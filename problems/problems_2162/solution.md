# [Python] 记录一下直接莽的BFS解法

> slug: python-ji-lu-yi-xia-zhi-jie-mang-de-bfsj-1tby
> date: 2022-02-06
> tags: Python, Python3
> question: Minimum Cost to Set Cooking Time (minimum-cost-to-set-cooking-time)
> url: https://leetcode.cn/problems/minimum-cost-to-set-cooking-time/solutions/1aUSH7/python-ji-lu-yi-xia-zhi-jie-mang-de-bfsj-1tby/

---
### 解题思路
其实直接分类讨论几种时间的最短耗时就好

### 代码
```python3
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        # number, minute, second, cost, idx, last
        queue = [(0, startAt, 0, 0, 0, False)]
        while queue:
            cost, num, minute, second, idx, last = heapq.heappop(queue)
            if minute * 60 + second == targetSeconds:
                return cost
            elif minute * 60 + second > targetSeconds or idx == 4:
                continue
            for i in range(idx, 4):
                if i == 3:
                    heapq.heappush(queue, (cost + pushCost,num, minute * 10 + second // 10, second % 10 * 10 + num, i + 1, False))
                elif i == 2:
                    heapq.heappush(queue,(cost + pushCost,num, second // 10, second % 10 * 10 + num, i + 1, False))
                elif i == 1:
                    heapq.heappush(queue,( cost + pushCost, num, minute, second * 10 + num, i + 1, False))
                else:
                    heapq.heappush(queue,( cost + pushCost,num, minute, num, i + 1, False))
            if not last:
                for other in range(10):
                    if other == num:
                        continue
                    heapq.heappush(queue,(cost + moveCost,other, minute, second, idx, True))
        return -1
```
```python3
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def calc(time):
            cost = pushCost * len(time)
            cur = str(startAt)
            for i in range(len(time)):
                if time[i] != cur:
                    cost += moveCost
                    cur = time[i]
            return cost
        
        #  参考灵老师直接cv的
        ans = inf
        if 60 <= targetSeconds < 6000:
            ans = calc(f"{targetSeconds // 60}{targetSeconds % 60 :02}")
        if targetSeconds < 100:
            ans = min(ans, calc(str(targetSeconds)))  # 仅输入秒数
        elif targetSeconds % 60 < 40:
            ans = min(ans, calc(f"{targetSeconds // 60 - 1}{targetSeconds % 60 + 60}"))  # 借一分钟给秒数
        return ans

```