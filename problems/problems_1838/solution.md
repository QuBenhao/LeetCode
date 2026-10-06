# [Python] Sliding window

> Author: Benhao
> Date: 2021-07-19
> Upvotes: 11
> Tags: Python, Python3

---

### Approach
After sorting, for each right endpoint j, find the leftmost i such that k operations can raise every value in the window to nums[j].
For each `j`, find the smallest `i` satisfying `nums[j] * (j - i + 1) <= k + nums[i] + nums[i+1] + ... + nums[j-1] + nums[j]`.
Add the right endpoint's value each time. If the inequality holds, the window length is a candidate answer; otherwise, advance the left endpoint `i` (the difference between if and while is explained below).
<br>
Why use `if` to move only once instead of `while`?
If the current i and j fail the inequality, moving i once preserves the previous window length. After finding the longest window, later windows may remain invalid, but the answer length stays fixed: we only need to look for a longer valid window.
Using while instead requires a variable to record the maximum answer.

### Code

Using if
```python3
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = j = 0
        # After sorting, the condition becomes nums[j] * (j - i + 1) <= k + presum[j + 1] - presum[i]
        for j, num in enumerate(nums):
            k += num
            if k < num * (j - i + 1):
                k -= nums[i]
                i += 1
            # This window may be invalid, but a valid window of the same length has already existed
        return j - i + 1
```
Using while
```python3
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = ans = 0
        # After sorting, the condition becomes nums[j] * (j - i + 1) <= k + presum[j + 1] - presum[i]
        for j, num in enumerate(nums):
            k += num
            while k < num * (j - i + 1):
                k -= nums[i]
                i += 1
            # Leftmost valid i for the current j
            ans = max(ans, j - i + 1)
        return ans
```
