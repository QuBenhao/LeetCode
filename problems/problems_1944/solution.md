# [Python] Monotonic stack

> Author: Benhao
> Date: 2021-07-24
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
Maintain a monotonic stack while traversing backward.

A person can see every shorter person popped from the stack, in increasing height order. If a taller person remains, only that first taller person is visible; all farther people are blocked.

### Code

```python3
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0] * n
        min_stack = []
        for i in range(n-1, -1, -1):
            h = heights[i]
            count = 0
            while min_stack and min_stack[-1] < h:
                min_stack.pop()
                count += 1
            if len(min_stack):
                count += 1
            ans[i] = count
            min_stack.append(h)
        return ans

```
