# [Python] 记忆化dfs 到 自底向上的动态规划 到 数学规律?

> Author: Benhao
> Date: 2021-05-12
> Upvotes: 14
> Tags: Python, Python3

---

### 解题思路
lru_cache永远滴神

其实用一维dp可以实现同样自底向上的递推。
**我们注意到:**
> 下一个状态的位置由它上一个状态的位置的两边及自己所得，即`dp[j] = dp[j-1] + dp[j] + dp[j+1]`
>
> `steps`的范围**远小于**`arrLen`! 那么如果arrLen足够大，我们有可能走到头再走回来吗？不存在的
> 其实走到最远再走回来只能是**step的一半的长度**
> 所以我们的dp数组长度取`steps//2`和`arrLen`之间的最小值，arrLen多余的部分不管怎么更新也不会影响结果了。
>
> 初始赋值一步的两个1，加上两个边界0，齐活。
>
> 一点点时间上的优化，dp数组最多更新到当前`i(能走到的距离)`和`steps-i(走得回来的距离)`和`数组长度的最小值`

**题外话：结果中的对称性** (思路来自[曙光磁铁](https://leetcode.cn/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/solution/ostepssuan-fa-zai-xian-qiu-jiao-shu-xue-mz6i2/))
> 从终点行往回推的过程，其实和从起点行往下推的过程是一样的，他们满足对称性。
>
> 比如: steps = 6, arrLen = 4的输入中
> 
> 结果为 【乘积左边的数是类似杨辉三角里的数，右边的数是它最终在答案里出现了多少次】
>
> 51 * 1(第六行) 
> 
>   = 21 * 1 + 30 * 1 （第五行）
> 
>    = 9 * 2 + 12 * 2 + 9 * 1 （第四行）
> 
>    = 4 * 4 + 5 * 5 + 3 * 3 + 1 * 1 （已经到达中间行）
>
>    = 2 * 9 + 2 * 12 + 1 * 9 （其实到这我们就发现是将对称位置的乘积倒着写了）
> 
>    = 1 * 21 + 1 * 30 （第二行）
>
>    = 1 * 51 （初始行）
>
> 于是就有了只计算到step的一半（中间行）的dp，然后直接求最终结果
> 
> 这个运算时间已经稳定100%了，如果能推出O(1)的计算公式还能更快


### 代码

```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @lru_cache(None)
        def dfs(cur, s):
            if cur == -1 or cur == arrLen or cur > s:
                return 0
            if cur <= 1 and s == 1:
                return 1
            s -= 1
            return dfs(cur, s) + dfs(cur-1,s) + dfs(cur+1,s)

        return dfs(0, steps) % (10 ** 9 + 7)
```
自底向上的dp
```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # 一维数组动态规划，自底向上滚动更新
        if arrLen == 1 or steps == 1:
            return 1
        dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        n = len(dp)
        dp[1] = dp[2] = 1
        for i in range(1, steps):
            nxt_dp = [0] * n
            for j in range(1, min(n - 1, i + 3, steps - i + 1)):
                nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
            dp = nxt_dp
        return dp[1] % (10 ** 9 + 7)
```

利用数学规律只求一半dp，目前还没有想到如何直接求得结果。
```python3
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # 一维数组动态规划，自底向上滚动更新
        if arrLen == 1 or steps == 1:
            return 1
        dp = [0] * (min(steps // 2 + 1, arrLen) + 2)
        n = len(dp)
        dp[1] = dp[2] = 1
        # 数学规律：对称性，只需要找到steps一半位置的dp的样子即可计算结果，因为后面往位置0递归算和从位置0递归算过来是一样的
        for i in range(1, steps // 2):
            nxt_dp = [0] * n
            for j in range(1, min(n - 1, i + 3)):
                nxt_dp[j] = dp[j-1] + dp[j] + dp[j+1]
            dp = nxt_dp
        # 偶数行是它的中心行的平方和
        if steps % 2 == 0:
            return sum(x**2 for x in dp) % (10 ** 9 + 7)
        # 奇数行实际上是它中心两行的点乘结果
        return sum(dp[i] * (dp[i-1] + dp[i] + dp[i+1]) for i in range(1,len(dp)-1)) % (10 ** 9 + 7)
```