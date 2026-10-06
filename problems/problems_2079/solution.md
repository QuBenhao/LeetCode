# [Python/Go] Simulation

> Author: Benhao
> Date: 2021-11-21
> Upvotes: 1
> Tags: Go, Python, Python3

---

### Approach
Go back to refill when there is not enough water.

### Code

```python3 []
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans, cur = 0, capacity
        for i, plant in enumerate(plants):
            if cur < plant:
                cur = capacity
                ans += 2 * i + 1
            else:
                ans += 1
            cur -= plant
        return ans
```
```go []
func wateringPlants(plants []int, capacity int) int {
    ans, cur := 0, capacity
    for i, v := range plants {
        if cur < v {
            cur = capacity
            ans += 2 * i + 1
        } else{
            ans += 1
        }
        cur -= v
    }
    return ans
}
```
