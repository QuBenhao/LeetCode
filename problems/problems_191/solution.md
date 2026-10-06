# [Python] Count 1 bits from right to left with n&n-1

> Author: Benhao
> Date: 2021-03-22
> Upvotes: 4
> Tags: Python

---

### Approach
n&n-1 clears the rightmost 1 bit. 
Count how many times this can be done.
For example, `101000`&`100111` = `100000`

### Code

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans

```
