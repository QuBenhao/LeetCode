# [Python] Prefix sums + hashing

> Author: Benhao
> Date: 2021-07-07
> Upvotes: 13
> Tags: Python, Python3

---

### Approach
To find all subarrays whose sum is goal, we naturally look for all prefix-sum indices i and j satisfying presum[j] - presum[i] == goal.
But finding i and j with nested scans takes o($n^2$).

Use Counter to count earlier prefix sums satisfying presum[i] == presum[j] - goal, and accumulate those counts into the answer.
Here, a prefix sum is also a count of ones.

### Code

```python3
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        countOnes = ans = 0
        cnts = Counter({0:1})
        for num in nums:
            countOnes += num
            ans += cnts[countOnes - goal]
            cnts[countOnes] += 1
        return ans
```
