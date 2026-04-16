# [Python] 转化为正负求和的证明 (数学归纳法)

> Author: Benhao
> Date: 2021-06-07
> Upvotes: 14
> Tags: Python, Python3

---

### 解题思路
两个石子$a$和$b$最好理解，最终结果要么是$a-b$要么是$b-a$.(取决于哪个是非负的所以写作$abs(a-b)$)

假设我们有三个石子, $a,b,c$ 且 $a \leq b \leq c$.
三种粉碎方法分别为 $(a,b),c$; $(a,c),b$; $(b,c),a$.
根据大小关系，三种结果分别为$a-b+c, abs(c-a-b), abs(c-b-a)$

我们只是要比较他们中更小的那个.

更一般的，对于$i$个石子，$s_1,s_2,..,s_i$，**最终结果必然在某种正负取石子中 （下文中简写为正负求和）**。
($i=2$和$i=3$的情况就是上面举的例子了)

证明: 假设$i$个石子的时候成立，$i+1$个石子的时候也成立。
对于石子$s_1,s_2,..,s_{i+1}$，我们任意选两个石子进行粉碎，假设粉碎的是$s_m$和$s_n$ 不妨设$sm \leq sn$,
我们变成了对 $s_1, s_2, .., s_{m-1}, s_{m+1}, .., s_{n-1}, s_{n+1}, .. s_{i+1}, s_n-s_m$ 的 $i$个石子求解。
根据假设,$i$个石子的答案存在于 $s_1, s_2, ... , s_n-s_m$的某种正负求和。
我们的最终结果，$s_1, s_2, .., s_{m-1}, s_{m+1}, .., s_{n-1}, s_{n+1}, .. s_{i+1}$的部分已经保证是原来石子中的正负求和了，
那么我们来看$s_n-s_m$的最终符号,
如果$s_n-s_m$符号为正,我们可以完全可以理解为对于$s_m$石子符号为负，$s_n$石子为正;同理,另一种情况为，$s_m$符号为正,$s_n$符号为负。
于是对于任意的石子$s_m$和$s_n$, $m,n \in 1,2,3,...,i+1$，我们最终的结果都是对于$i+1$个石子的正负求和。

证毕。

也就是**对于n个石子答案始终在正负求和中**。

根据这个证明，原题可以理解为:将原来的石子分成两堆$positive$和$negative$的和，并使得他们和的差值的绝对值$abs(positive - negative)$尽可能的小。

到这里就可以理解为什么这题可以转换为01背包问题了。

昨天的代码涂涂改改又是一天。

### 代码

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == len(stones):
                return curr if curr >= 0 else inf
            return min(dfs(idx+1, curr+stones[idx]), dfs(idx+1, curr-stones[idx]))
        return dfs(0, 0)
```

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 贪心: 最接近 sum//2 的组合和
        @lru_cache(None)
        def dfs(idx, curr):
            if curr > t:
                return 0
            if idx == n:
                return curr
            return max(dfs(idx+1, curr + stones[idx]),dfs(idx+1, curr))
        
        n = len(stones)
        s = sum(stones)
        t = s // 2
        return s - 2 * dfs(0, 0)
```

```python3
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 贪心: 最接近 sum//2 的组合和
        s = sum(stones)
        t = s // 2
        sums = {0}

        for stone in stones:
            for cs in list(sums):
                if cs + stone < t:
                    sums.add(cs + stone)
                elif cs + stone == t:
                    return s - 2 * t
        return s - 2 * max(sums)
```