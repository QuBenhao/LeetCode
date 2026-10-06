# [Python] Modular congruence with delayed insertion of prefix sums

> Author: Benhao
> Date: 2021-06-02
> Upvotes: 42
> Tags: Python, Python3

---

### Approach
At first, seeing a medium problem, I naturally tried brute force. The code below updates the remainders of every sum ending at the current number and, unsurprisingly, exceeds the time limit.
```python3
        dp = set()
        temp = None
        for num in nums:
            if k - num % k in dp:
                return True
            dp = set((t + num) % k for t in dp)
            if temp is None:
                temp = num % k
            else:
                temp = (temp+num) % k
                if not temp:
                    return True
                dp.add(temp)
                temp = num % k
        return False
```

An O(n) solution cannot update every remainder in dp as above. Since this concerns sums of contiguous subarrays, it must involve a difference of prefix sums.
To check whether the interval [i,j] satisfies `(presum[j] - presum[i]) % k == 0`, we need `presum[j] % k == presum[i] % k`. This is modular congruence.
The subarray must have length at least 2, so record the remainders of all prefix sums at least two positions before the current one.
Use `delayed insertion`: first check for a prefix sum congruent to the current one, then add the previous prefix sum to the set.


### Code

```python3
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # Current prefix sum
            presum += num
            presum %= k
            # Modular congruence
            if presum in modes:
                return True
            # The previous prefix sum can be used on the next iteration, when it is two positions away
            modes.add(last)
        return False

```
