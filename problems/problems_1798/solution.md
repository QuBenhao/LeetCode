# [Python] Sorting and prefix sums: a detailed derivation

> Author: Benhao
> Date: 2021-03-21
> Upvotes: 2
> Tags: Python

---

### Approach
We need to build sums from small to large, suggesting sorting: small sums need small coins, and larger coins cannot help yet.
The largest sum an array can form is its total, so each prefix's maximum is its prefix sum. This suggests persum, though a running total also works. If every value up to the current sum is constructible and coins[i] <= ans, combining coins[i] with earlier constructions gives every value from coins[i] through coins[i] + persum[i-1], namely persum[i].

Once coins[i] > ans, the current ans cannot be formed: earlier coins reach only persum[i-1], while coins[i] is too large to form persum[i-1]+1.

The running ans can replace the prefix-sum array, giving the simplified second implementation.

### Code

```python
class Solution(object):
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        coins.sort()
        persum = [0] * len(coins)
        ans = 1
        for i,c in enumerate(coins):
            persum[i] += persum[i-1] + c

        if persum[0] != 1:
            return ans
        ans += 1
        for i in range(1,len(persum)):
            if persum[i] == ans:
                ans += 1
            elif coins[i] <= ans:
                ans = persum[i] + 1
            else:
                return ans
        return ans
```

Simplified version
```python
    def getMaximumConsecutive(self, coins):
        """
        :type coins: List[int]
        :rtype: int
        """
        ans = 1
        for coin in sorted(coins):
            if coin <= ans:
                ans += coin
            else:
                return ans
        return ans
```
