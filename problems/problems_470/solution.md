# [Python/Java] Sharing lee's approach with an expected 1.183 calls to rand7

> Author: Benhao
> Date: 2021-09-05
> Upvotes: 11
> Tags: Java, Python, Python3

---

### Approach
The official and other solutions have good ideas, but discard too many random outcomes, increasing the expected number of calls. The theoretical optimum is $log_{7}10 = 1.183$, which requires [lee215's solution](https://leetcode.com/problems/implement-rand10-using-rand7/discuss/151567/C%2B%2BJavaPython-1.183-Call-of-rand7-Per-rand10)
using powers of 7.

My understanding is this: $7^{19} = 11398895185373143$. As when generating 49 outcomes and discarding 40-48, discarding the excess here leaves 11398895185373140 outcomes that generate at least one random number, with probability 99.99999999999997%. Values below 10000000000000000 can be represented by 16 decimal digits, each equally likely to be 0-9, so there is an 87.73% chance of generating 16 random numbers.

I do not fully understand this solution yet and would appreciate an explanation.

### Code

```Python3 []
class Solution:
    cache, upper = 0, 1
    def rand10(self):
        while self.upper < 10**9:
            self.cache, self.upper = self.cache * 7 + rand7() - 1, self.upper * 7
        res = self.cache % 10 + 1
        self.cache, self.upper = self.cache // 10, self.upper // 10
        return res
```
```Java []
class Solution extends SolBase {
    long cache = 0L, range = 1L;
    public int rand10() {
        while(range < 1e9){
            cache = cache * 7 + rand7() - 1;
            range *= 7;
        }
        long tmp = cache;
        cache /= 10;
        int res = (int)(tmp - cache * 10) + 1;
        range /= 10;
        return res;
    }
}
```
