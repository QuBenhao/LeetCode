# [Python] Learning the O(n) solution

> slug: by-himymben-vl4n
> date: 2022-05-04
> tags: Python, Python3
> question: Count Subarrays With More Ones Than Zeros (count-subarrays-with-more-ones-than-zeros)
> url: https://leetcode.cn/problems/count-subarrays-with-more-ones-than-zeros/solutions/CEgCcJ/by-himymben-vl4n/

---
### Approach
Maintain the number of valid subarrays in a variable, updating it by the boundary changes whenever the sum changes by +1 or -1.

### Code

```python3
MOD = int(1e9) + 7
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        # Counts of prefix sums
        cnts = Counter()
        cnts[0] = 1
        # cnt tracks the number of valid subarrays (each change is only +1 or -1, so only the boundary change matters)
        ans = cnt = s = 0
        for num in nums:
            if num:
                # Count of prefix sums equal to s: the current sum is about to increase by one, so each such prefix forms a valid subarray ending here
                cnt += cnts[s]
                s += 1
            else:
                # Count of prefix sums equal to s + 1: the current sum is about to decrease by one, so these prefixes no longer form valid subarrays ending here
                s -= 1
                cnt -= cnts[s]
            cnts[s] += 1
            ans = (ans + cnt) % MOD
        return ans
```
