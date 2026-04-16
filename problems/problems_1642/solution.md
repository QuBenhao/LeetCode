# [Python] 最大堆

> Author: Benhao
> Date: 2021-05-31
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
有点儿像每回合打怪那个题，先欠着，统计所有需要用的砖头数，如果砖头数不够了，从最大的砖头数里补回来（当时应该使用梯子）

### 代码

```python3
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        for i in range(n-1):
            if heights[i+1] <= heights[i]:
                continue
            diff = heights[i+1] - heights[i]
            heapq.heappush(pq, -diff)
            bricks -= diff
            if bricks < 0 and ladders:
                ladders -= 1
                bricks -= heapq.heappop(pq)
            elif bricks < 0:
                return i
        return n - 1

```