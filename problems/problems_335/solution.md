# [Python] Adapting another solution today

> slug: python-fan-yi-guan-by-himymben-c85r
> date: 2021-10-28
> tags: Python, Python3
> question: Self Crossing (self-crossing)
> url: https://leetcode.cn/problems/self-crossing/solutions/6xbf6y/python-fan-yi-guan-by-himymben-c85r/

---
### Approach
I do not want to dwell on this problem today; it seems to require enumerating the crossing cases. I am translating [三叶姐姐's solution](https://leetcode.cn/problems/self-crossing/solution/gong-shui-san-xie-fen-qing-kuang-tao-lun-zdrb/).

### Code

```python3
class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        l = len(distance)
        if l <= 3:
            return False
        for i in range(3, l):
            # The fourth segment intersects the first (applies to any pair three positions apart)
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # The fifth segment intersects the first (applies to any pair four positions apart)
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
            # The sixth segment intersects the first (applies to any pair five positions apart)
            if i >= 5 and distance[i-2] - distance[i-4] >= 0 and distance[i] >= distance[i-2] - distance[i-4] and distance[i-1] >= distance[i-3] - distance[i-5] and distance[i-1] <= distance[i-3]:
                return True
        return False
```
