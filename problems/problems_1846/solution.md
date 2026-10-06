# [Python] Understanding the problem: o(nlogn) -> o(n)

> Author: Benhao
> Date: 2021-07-14
> Upvotes: 18
> Tags: Python, Python3

---

### Approach
The first element is 1, the second is at most 2, the third at most 3, and the n-th at most n.

Values can only decrease, so not every position can attain that bound.
Use the idea of Tian Ji's horse race: sort, match small values to small positions and large values to large positions, reducing each as little as possible. Then find the largest achievable final value.

### Code

```python3
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        limit = 1
        for num in sorted(arr)[1:]:
            limit = min(limit + 1, num)
        return limit
```
Sorting is unnecessary; maintain an array counting values from 1 through n.
In Python, two passes may not run faster than the version above, though the asymptotic complexity is lower.
```python3
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnts = [0] * (n + 1)
        for num in arr:
            cnts[min(num, n)] += 1
        limit = 0
        for i in range(1, n + 1):
            limit = min(i, limit + cnts[i])
        return limit
```
