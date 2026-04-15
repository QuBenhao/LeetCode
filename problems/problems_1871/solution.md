# [Python] 记忆化搜索 100%

> Author: Benhao
> Date: 2021-05-23
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
超时其实主要是因为存在连续长度大于最大跳跃距离的超长的case，和第一题很像的方法就可以判断他们为False了。
其实解决超时主要就是需要额外的提前返回整个dfs的结果为False，而不是继续搜索。

### 代码

```python3
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i == n - 1:
                return True
            if s[i] == '1' or n - 1 - i < minJump:
                return False
            for j in range(min(i+maxJump,n-1), i+minJump-1,-1):
                if dfs(j):
                    return True
            return False

        if s[-1] == '1':
            return False
        if len(max(re.split('0+',s),key=len)) >= maxJump:
            return False
        n = len(s)
        return dfs(0)
```