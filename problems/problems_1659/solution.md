# [Python] 记忆化dfs 

> Author: Benhao
> Date: 2021-05-30
> Upvotes: 6
> Tags: Python, Python3

---

### 解题思路
按格子遍历，参考自[Java的记忆化搜索](https://leetcode.cn/problems/maximize-grid-happiness/solution/dong-tai-gui-hua-shi-jian-qia-de-you-dian-er-jin-y/)

遍历每个格子填入有三种选择，不填或者填内向的人或者填外向的人。
state没必要记录整个m*n的格子，因为自左到右，自顶向下填的时候，**每个格子相邻的存在人的只有可能是上边或者左边**，而上边到左边的跨度正好是`列数n`。
所以我们只需要知道最近的`n`个格子的填入情况，就可以统计幸福度的变化。

用`0`代表空,`1`代表填入内向，`2`代表填入外向。
统计幸福值的时候，注意格子贴着左边的时候是没有左边的人即可。

### 代码

```python3
class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        @lru_cache(None)
        def dfs(x, y, intro, extro, state):
            if y == n:
                return dfs(x+1,0, intro, extro, state)
            if x == m:
                return 0
            # 最近的n个安排，再多不会被当前的影响到
            l = list(state)
            # 上面的人是l[0]，左边的人是l[-1]

            # 什么也不填
            ans = dfs(x,y+1,intro,extro, tuple(l[1:] + [0]))

            # 填入一个内向
            if intro:
                diff = 120
                if l[0] == 1:
                    diff -= 30 * 2
                elif l[0] == 2:
                    # 一个内向一个外向
                    diff -= 10
                if y:
                    if l[-1] == 1:
                        diff -= 30 * 2
                    elif l[-1] == 2:
                        diff -= 10
                ans = max(ans, dfs(x,y+1, intro-1, extro, tuple(l[1:] + [1])) + diff)
            
            # 填入一个外向
            if extro:
                diff = 40
                if l[0] == 1:
                    diff -= 10
                elif l[0] == 2:
                    diff += 40
                if y:
                    if l[-1] == 1:
                        diff -= 10
                    elif l[-1] == 2:
                        diff += 40
                ans = max(ans, dfs(x,y+1, intro, extro - 1, tuple(l[1:] + [2])) + diff)
            return ans
        
        return dfs(0, 0, introvertsCount, extrovertsCount, tuple([0] * n))
```