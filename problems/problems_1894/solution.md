# [Python/Java] Prefix sums + binary search

> Author: Benhao
> Date: 2021-09-09
> Upvotes: 7
> Tags: Java, Python, Python3

---

### Approach
Chalk consumption repeats cyclically, so replace k with k modulo the total consumption without changing the answer, effectively skipping full rounds.
Find which student exhausts this remainder by binary searching its position in the prefix sums.

### Code

```Python3 []
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        return bisect_right((presum := list(accumulate(chalk))), k % presum[-1])
```
```Java []
class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        int n = chalk.length;
        long[] presum = new long[n];
        for(int i=0;i<n;i++)
            presum[i] = chalk[i] + (i > 0 ? presum[i-1] : 0);
        k %= presum[n-1];
        int l = 0, r = n - 1;
        while(l < r){
            int mid = l + r >> 1;
            if(presum[mid] <= k)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
}
```
