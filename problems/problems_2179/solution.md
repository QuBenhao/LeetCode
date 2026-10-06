# [Python] Increasing triplets

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 8
> Tags: Python, Python3

---

### Approach
Transform the problem by mapping each value in one array to its index and replacing the values in the other array with those indices.
This reduces the problem to counting increasing triplets in a single array.
The mapped indices are ordered by position in the first array, so an increasing triplet in the transformed second array also satisfies the increasing-position condition in the first.


After this transformation, the problem resembles finding a longest increasing subsequence.
For example 1, nums1 gives the mapping 2->0, 0->1, 1->2, 3->3. Replacing nums2 yields [1,2,0,3].
To count increasing triplets in nums2, maintain the values already visited and quickly count those smaller than the current value. A monotonic stack comes to mind, but inserting must not replace existing values, so use SortedList.


There are idx visited values smaller than the current value, and len(sl) visited values in total. The number of increasing triplets with this point in the middle is $idx * (n - 1 - i - len(sl) + idx)$.
[There are $n - 1 - i$ values greater than $i$, of which $len(sl) - idx$ have already been visited.]

### Code

```python3
from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n, idx_map = len(nums1), {num:i for i, num in enumerate(nums1)}
        for i in range(n):
            nums2[i] = idx_map[nums2[i]]
        sl, ans = SortedList(), 0
        for i in nums2:
            idx = sl.bisect_left(i)
            ans += idx * (n - 1 - i - len(sl) + idx)
            sl.add(i)
        return ans
```
