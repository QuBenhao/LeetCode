# [Python] 动态规划

> Author: Benhao
> Date: 2021-08-18
> Upvotes: 7
> Tags: Python, Python3

---

### 解题思路

维护各种状态以及他们的递推关系。

> alast: 当前有A出现了，且结尾不是L(A或P)，那么它初始为1，递推关系满足由所有不带A的里面加入一个A(所以是上一次不带A的和)以及所有带A的里面加入一个P(所以是上一次带A的和)。
> alastL: 当前有A出现了，且结尾是一个L(AL或PL)，那么它初始为0，递推关系满足由上一个带A的且结尾不是L加入一个L得到。
> alastLL: 当前有A出现了，且结尾是LL，那么它初始为0，递推关系满足由上一个带A的且结尾是一个L的加入一个L得到。
> last: 当前没有A，且结尾不是L(P)，那么它初始为1，递推关系满足由上一个所有不带A的里面加入一个P得到。
> lastL: 当前没有A，且结尾是一个L，递推关系满足由不带A的且结尾没有L的里面加入一个L得到。
> lastLL: 当前没有A, 且结尾是两个L, 递推关系满足由不带A的且结尾是一个L的里面加入一个L得到。

### 代码

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

numpy矩阵快速幂
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