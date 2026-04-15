# [Python] 动态规划 & 记忆化搜索 2000ms -> 32ms 的过程

> Author: Benhao
> Date: 2021-07-06
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
我们要在某一层$x$扔这个鸡蛋,鸡蛋可能碎了，也可能没碎; 如果鸡蛋碎了，那么结果必然在小于$x$的层里;否则,结果必须在高于$x$的层里；
前者问题就变为用$k-1$个鸡蛋，解决$x-1$层;后者问题就变为用$k$个鸡蛋解决$n-x$层。
由于我们要解决全部的可能性，所以我们要取这两者的最大值: 故扔在该层的最终结果为`dp[k-1][x-1], dp[k][n-x]`中的最大值，加上我们扔这个鸡蛋的操作1.

但是我们不知道扔在哪层，也就是$x$是多少对于解决$k,n$最好的解。
初步想法是遍历找所有楼层的扔法中最小的那个。
也就是`dp[k][n] = min(max(dp[k-1][x-1], dp[k][n-x]) for x in range(1, n)) + 1`。

这样每次都需要遍历n来找到最大值，会超时。
有没有优化的办法呢？

我们知道在有相同鸡蛋的时候，需要检测的层数越多，最终需要的操作次数也就越多。也就是说当x变大的时候，左边变大了；而右边变小了。
这种感觉就像是左边是一条从小到大的线，右边是一条从大到小的线，而最终结果必然在交点附近。
根据这种单调性，我们可以想到利用二分查找来加速找到最合适的$x$的位置。
如果当前是k-1,x-1这边更大，那么我们需要再看看x变小;相反如果是k,n-x这边更大，我们需要再看看x变大。
于是得到了第一段代码 (2000ms)。

<br>
发现这种写法提交后有点儿慢，于是又开始思考其他人是怎么写的那么快的算法。
想到了从另一种角度考虑这个问题。
鸡蛋还是要扔的，它也还是可能碎也可能没碎。但是呢，如果这次我们关注于尝试次数，也就是说，我们有$k$个鸡蛋,最多$m$次尝试次数，我们能最多检测多少层呢？
显然如果鸡蛋碎了，那么我们还能使用$k-1$个鸡蛋，还有$m-1$次尝试次数；如果鸡蛋没碎，我们就还能使用$k$个鸡蛋，但尝试次数还是要变为$m-1$。再加上我们扔鸡蛋的这层.
也就是说`dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1`。
我们只要找到最小的m，使得dp[k][m] >= n即可。
于是有了第二段代码 (700ms)。

<br>
性能好像还是不够好，因为我们可能反复计算了很多次同样的k和m。
故最终使用记忆化搜索解决重复搜索同样的问题的解得到第三段代码 (32ms)。

### 代码

```python3
class Solution:
    @lru_cache(None)
    def superEggDrop(self, k: int, n: int) -> int:
        if k == 1 or n <= 2:
            return n
        # 如果k比n大，我们可以每个楼层用一个鸡蛋，最快的方法就是二分
        if k >= n:
            return int(log(n, 2)) + 1
        # 假设初始扔的第一个楼层为x,如果鸡蛋碎了，那么问题变为用k-1个鸡蛋解决x-1个楼层; 如果没碎，问题变为k个鸡蛋解决n-x个楼层
        # 如果x越大，左边越大，右边越小; x越小左边越小，右边越大
        ans = n
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            l = self.superEggDrop(k-1,mid-1)
            r = self.superEggDrop(k, n-mid)
            ans = min(ans, max(l, r) + 1)
            if l >= r:
                right = mid
            else:
                left = mid + 1
        return ans
```

```python3
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 反过来想，给我们k个鸡蛋，m次尝试机会，我们最多能测出多少层？
        # 我们扔一个鸡蛋，鸡蛋可能碎了，也可能没碎。
        # 如果鸡蛋没碎，我们就能解决dp[k][m-1]层；如果鸡蛋碎了，我们就能解决dp[k-1][m-1]层;再加上第一个扔的层。
        # 有: dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1.
        # 问题变为求最小的使得dp[k][m] >= n
        dp = [[0] * (n + 1) for _ in range(k+1)]
        dp[1][1] = 1
        for i in range(1, k+1):
            for j in range(1, n+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + 1
                if i == k and dp[i][j] >= n:
                    return j
        return n
```

```python3
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        # 反过来想，给我们k个鸡蛋，m次尝试机会，我们最多能测出多少层？
        # 我们扔一个鸡蛋，鸡蛋可能碎了，也可能没碎。
        # 如果鸡蛋没碎，我们就能解决dp[k][m-1]层；如果鸡蛋碎了，我们就能解决dp[k-1][m-1]层;再加上第一个扔的层。
        # 有: dp[k][m] = dp[k][m-1] + dp[k-1][m-1] + 1.
        # 问题变为求最小的使得dp[k][m] >= n
        for i in range(1, n+1):
            if self.maximumFloors(k, i) >= n:
                return i
        return n
    
    @lru_cache(None)
    def maximumFloors(self, k, m):
        if k == 0:
            return 0
        if m == 1:
            return 1
        return self.maximumFloors(k, m-1) + self.maximumFloors(k-1,m-1) + 1
```