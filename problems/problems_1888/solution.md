# [Python] 统计01前缀和和10前缀和

> Author: Benhao
> Date: 2021-06-06
> Upvotes: 6
> Tags: Python, Python3

---

### 解题思路
pre01[i+1] 代表0到i的字符与010101的区别的个数。其余同理。

n为偶数的情况很简单，要么前半截要1010，后半截也要1010，要么就是都要0101,所以返回两者的最小值即可。
奇数的时候枚举每个放到后面不同的长度需要的操作次数。

### 代码

```python3
class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        pre01 = [0] * n
        pre10 = [0] * n
        for i,c in enumerate(s):
            if c == '1':
                if i % 2 == 0:
                    pre01[i] = pre01[i-1] + 1
                    pre10[i] = pre10[i-1]
                else:
                    pre10[i] += pre10[i-1] + 1
                    pre01[i] = pre01[i-1]
            else:
                if i % 2 == 0:
                    pre10[i] += pre10[i-1] + 1
                    pre01[i] = pre01[i-1]
                else:
                    pre01[i] = pre01[i-1] + 1
                    pre10[i] = pre10[i-1]
        pre01 = [0] + pre01
        pre10 = [0] + pre10
        if n % 2 == 0:
            return min(pre01[-1],pre10[-1])
        ans = float("inf")
        for i in range(n):
            # 把前面i个放到最后
            # 前面要10101，后面要010
            ans1 = pre01[-1] - pre01[i] + pre10[i]
            ans2 = pre10[-1] - pre10[i] + pre01[i]
            ans = min(ans, ans1, ans2)
        return ans
```