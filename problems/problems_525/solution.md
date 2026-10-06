# [Python] Prefix sum variable + dictionary

> Author: Benhao
> Date: 2021-06-03
> Upvotes: 54
> Tags: Python, Python3

---

### Approach
Use a dictionary to record the earliest position of each `difference between the number of ones and zeros`. Maintain a prefix sum variable for the `difference between the number of ones and zeros` seen so far.


Why does this work? Set aside the longest-length requirement for now.
What does it mean if the `difference between the number of ones and zeros` is equal at two positions?
Suppose the difference is `k`. If the prefix ending at the left position `x` has `m` zeros, it has `m+k` ones. Likewise, if the prefix ending at the right position `y` has `n` zeros, it has `n+k` ones.
Then the interval (x,y], open on the left and closed on the right, contains `n-m` zeros and `n+k-m-k=n-m` ones.
Thus, **the prefix differences at two positions are equal if and only if the interval between them contains equal numbers of zeros and ones**.


To find the longest interval, keep its left endpoint as far left as possible. If a difference already appears in the dictionary, do not update its position; only check the resulting length.

### Code

```python3
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Prefix sum dictionary: key is the difference between counts of ones and zeros; value is its index
        hashmap = {0:-1}
        # Current difference between counts of ones and zeros
        counter = ans = 0
        for i,num in enumerate(nums):
            # Each additional one increases the difference by 1
            if num:
                counter += 1
            # Each additional zero decreases the difference by 1
            else:
                counter -= 1
            # Equal prefix differences mean the interval between them contains equal numbers of ones and zeros!
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans

```
