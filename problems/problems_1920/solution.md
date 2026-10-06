# [Python] Implement directly

> Author: Benhao
> Date: 2021-07-04
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Simulation

### Code

```python3
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[nums[i]] for i in range(len(nums))]
```
