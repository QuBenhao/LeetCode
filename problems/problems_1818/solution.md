# [Python] Simulation: sort, then binary search

> Author: Benhao
> Date: 2021-07-13
> Upvotes: 33
> Tags: Python, Python3

---

### Approach
For each value in nums2, find the closest value in nums1 and compute the sum of absolute differences after replacing with it. Return the minimum.

> In detail:
Compute the original sum of absolute differences and return immediately if it is 0. Otherwise, iterate over each position, binary search for its best replacement, compute the new sum, and update the minimum.

### Code

```python3
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        if not diff:
            return 0
        ans = inf
        sl = sorted(nums1)
        for i, num in enumerate(nums2):
            idx = bisect.bisect_left(sl, num)
            # If idx > 0, try replacing the current value with the value at idx-1
            if idx:
                ans = min(ans, diff - abs(nums1[i] - nums2[i]) + abs(sl[idx-1] - nums2[i]))
            # If idx < n, try replacing the current value with the value at idx
            if idx < n:
                ans = min(ans, diff - abs(nums1[i] - nums2[i]) + abs(sl[idx] - nums2[i]))
        return ans % (10 ** 9 + 7)
```
The above code repeatedly includes the entire diff in comparisons. Track it separately and add it to the final answer instead, giving this single-loop implementation:
```python3
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n, total, sl, ans = len(nums1), 0, sorted(nums1), inf
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            idx = bisect.bisect_left(sl, nums2[i])
            # If idx > 0, try replacing the current value with the value at idx-1
            if idx:
                ans = min(ans, abs(sl[idx-1] - nums2[i]) - diff)
            # If idx < n, try replacing the current value with the value at idx
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total
```
