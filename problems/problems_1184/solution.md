# [Python/Java/C++/TypeScript/Go] 求和

> Author: Benhao
> Date: 2024-09-16
> Upvotes: 0
> Tags: Python3

---

```Python3 []
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(sum(distance) - s, s) if (s := sum(distance[min(start, destination):max(start, destination)])) >= 0 else 0
```
