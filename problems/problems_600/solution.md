# [Python/Java] Memoized recursion

> Author: Benhao
> Date: 2021-09-11
> Upvotes: 20
> Tags: Java, Python, Python3

---

### Approach
Given a binary number n, such as 10110, counting bit combinations without adjacent ones resembles House Robber, where adjacent houses cannot both be selected.
For numbers at most n, consider the first bit: it is either 1 or 0.

> If the first bit is 1, the second must be 0. If the original second bit is already 0, recurse on the remaining bits with their original upper bound, 110 in this example, to stay within n.
> If the original second bit is 1, we must set it to 0 because the first bit is 1. Any remaining bits then produce a number below n, so recurse with an all-ones upper bound, 111 here.
> If the first bit is 0, recurse with 1111 as the upper bound.


### Code

```Python3 []
class Solution:
    @lru_cache(None)
    def findIntegers(self, n: int) -> int:
        if n <= 3:
            return n + 1 if n < 3 else n
        bits = len(bin(n)) - 2
        return self.findIntegers((1<<(bits-1))-1) + (self.findIntegers((1<<(bits-2))-1) if (n >> (bits - 2)) & 1 else self.findIntegers(n - (1<<(bits-1))))
```
```Java []
class Solution {
    HashMap<Integer, Integer> dp = new HashMap<>();
    public int findIntegers(int n) {
        if(n < 4)
            return n < 3 ? n + 1 : n;
        if(dp.containsKey(n))
            return dp.get(n);
        int b = bits(n);
        // Count numbers whose first bit is 0
        int res = findIntegers((1 << b) - 1);
        // Count numbers whose first bit is 1 based on whether the second bit is 1
        res += ((n >> (b - 1)) & 1) == 1? findIntegers((1 << (b-1)) - 1) : findIntegers(n - (1 << b));
        dp.put(n, res);
        return res;
    }

    public int bits(int n){
        for(int i = 31; i > 0; i--)
            if(((n >> i) & 1) == 1)
                return i;
        return 0;
    }
}
```
