# [Python] 记忆化dfs

> Author: Benhao
> Date: 2021-05-24
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
递推的由来:
既然后面的打印会覆盖前面的，也就是说，如果开始字符串的两头各有一个'a'，那么我们打满'a'(后面总会覆盖)，和分别打两个'a'(中间相当于打满了空)在前后的效果是一样的，但是次数是不同的。
即打印'aba'和打印'ab'的次数一样。

如果首尾不同的话，我们总归是要分别打印他们的，而这个分别打印可以看做是对原字符串拆分成两个字符串来打印，关键是找到合理的拆分地方。
什么时候能节省打印次数呢？就又回到了上面的递推。

拆分k的地方还可以优化，最优的k应该是能节省打印次数的，会出现在k和i或者j相同的地方。

### 代码

优化前
```python3
class Solution:
    def strangePrinter(self, s: str) -> int:
        # 预处理，连续的由相同字符组成的子串看做一个,比如"aaabbb"和"ab"是没有区别的
        building = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                building.append(s[i])

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            # j和i是相同的，那么打印i到j和打印i到j-1所需的次数是一样的(或者说i+1到j)
            if building[i] == building[j]:
                return dfs(i, j - 1)
            # i和j是不同的,找到一个最优的拆分方式
            return min(dfs(i,k) + dfs(k+1,j) for k in range(i,j))

        return dfs(0, len(building) - 1)

```

优化后
```python3
        # 预处理，连续的由相同字符组成的子串看做一个,比如"aaabbb"和"ab"是没有区别的
        building = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                building.append(s[i])

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            # j和i是相同的，那么打印i到j和打印i到j-1所需的次数是一样的(或者说i+1到j)
            if building[i] == building[j]:
                return dfs(i, j - 1)
            # i和j是不同的,找到一个最优的拆分方式
            return min(dfs(i, k) + dfs(k + 1, j) for k in range(i, j)
                           if building[k] == building[i] or building[k] == building[j])

        return dfs(0, len(building) - 1)
```