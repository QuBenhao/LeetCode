# [Python] Dynamic programming

> Author: Benhao
> Date: 2021-08-18
> Upvotes: 7
> Tags: Python, Python3

---

### Approach

Maintain the different states and their recurrence relations.

> alast: An A has appeared, and the sequence does not end in L (it ends in A or P). Initialize to 1. Form this state by appending A to any sequence without A, or P to any sequence with A, so add the previous totals for both groups.
> alastL: An A has appeared, and the sequence ends in one L (AL or PL). Initialize to 0. Form this state by appending L to a sequence that contains A and does not end in L.
> alastLL: An A has appeared, and the sequence ends in LL. Initialize to 0. Form this state by appending L to a sequence that contains A and ends in one L.
> last: No A has appeared, and the sequence does not end in L (it ends in P). Initialize to 1. Form this state by appending P to any sequence without A.
> lastL: No A has appeared, and the sequence ends in one L. Form this state by appending L to a sequence without A that does not end in L.
> lastLL: No A has appeared, and the sequence ends in two Ls. Form this state by appending L to a sequence without A that ends in one L.

### Code

```Python3 []
class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10 ** 9 + 7
        alast, alastL, alastLL, last, lastL, lastLL = 1, 0, 0, 1, 1, 0
        for i in range(2, n + 2):
            alast, alastL, alastLL, last, lastL, lastLL = (alastLL + alastL + alast + last + lastL + lastLL) % mod,alast,alastL,(last + lastL + lastLL) % mod,last,lastL
        return alast
```
```Java []
class Solution {
    public int checkRecord(int n) {
        int mod = (int)1e9 + 7;
        int aLast = 1, aLastL = 0, aLastLL = 0, last = 1, lastL = 1, lastLL = 0, tmp0, tmp1, tmp2, tmp3, tmp4, tmp5;
        for(int i=2;i<=n+1;i++){
            tmp0 = (aLast + aLastL) % mod;
            tmp0 = (tmp0 + aLastLL) % mod;
            tmp0 = (tmp0 + last) % mod;
            tmp0 = (tmp0 + lastL) % mod;
            tmp0 = (tmp0 + lastLL) % mod;
            tmp1 = aLast;
            tmp2 = aLastL;
            tmp3 = (last + lastL) % mod;
            tmp3 = (tmp3 + lastLL) % mod;
            tmp4 = last;
            tmp5 = lastL;
            aLast = tmp0;
            aLastL = tmp1;
            aLastLL = tmp2;
            last = tmp3;
            lastL = tmp4;
            lastLL = tmp5;
        }
        return aLast;
    }
}
```

Fast matrix exponentiation with numpy
```Python3
import numpy as np
MOD = 10 ** 9 + 7
class Solution:
    def checkRecord(self, n: int) -> int:
        cell = np.diag([1] * 6)
        mul = np.array([[1,1,1,0,0,0],[1,0,0,0,0,0],[0,1,0,0,0,0],[1,0,0,1,1,1],[1,0,0,1,0,0],[0,0,0,0,1,0]])
        n -= 1
        while n:
            if n & 1:
                cell = np.mod(np.dot(cell, mul), MOD)
            mul = np.mod(np.dot(mul, mul), MOD)
            n >>= 1
        ans = np.mod(np.dot(cell, np.array([1,1,0,0,0,0])), MOD)
        return int((sum(ans) + ans[0]) % MOD)
```
