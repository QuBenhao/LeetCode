# [Python] 前缀+统计每个位置作为分界线 or 动态规划

> Author: Benhao
> Date: 2021-06-04
> Upvotes: 6
> Tags: Python, Python3

---

### 解题思路
**前缀暴力**
设想每个位置只要左边留'a'，右边留'b'的操作数;那么需要知道左边要删多少个'b'，右边要删多少个'a'；
故使用前缀和统计'a'的数量（'b'的数量自然就是长度减'a'的数量）
统计每个位置作为分界线需要的操作数，最终返回最小的。

**动态规划**
假设前面的字符串是平衡的，那么它要么是以'b’结尾，要么全是'a'。
到当前位置时，如果字符是'b'，是不影响平衡性的。
但如果字符是'a'，
要么是保留这个'a'，那么这种保留必须要删光之前所有的'b';
另一种选择是删掉这个'a'，不管之前是怎么样的，保留了原来的平衡性。

所以当前位置的最优解必然是`上一个的最优解+1`和`b的个数`中最小的那个。

### 代码

```python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        count = [0] * (n + 1)
        for i,c in enumerate(s):
            if c == 'a':
                count[i+1] = count[i] + 1
            else:
                count[i+1] = count[i]
        ans = float("inf")
        for i in range(n):
            # 到i有多少个'b'，后面有多少个'a'
            b = i - count[i]
            a = count[-1] - count[i+1]
            if not a and not b:
                return 0
            ans = min(ans, b+a)
        return ans
```

```python3
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # b的个数
        cnt = ans = 0
        for c in s:
            if c == 'b':
                # 'b'为结尾，必然不影响之前的平衡性
                cnt += 1
            else:
                # 'a'为结尾，要么是上一个的平衡结果再删掉这个'a',要么要删光前面的'b'
                ans = min(ans + 1, cnt)
        return ans
```