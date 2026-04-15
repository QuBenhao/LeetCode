# [Python] 记忆化搜索(dp)优化(100%)

> Author: Benhao
> Date: 2021-06-17
> Upvotes: 4
> Tags: Python, Python3

---

### 解题思路
在朴素搜索版本中，我们不使用left_dfs和right_dfs，所以我们每次都需要遍历查找最大值。
```python3
            left = idx - 1
            right = idx
            if presum[idx] == half:
                ans = max(ans, presum[idx] - presum[i] + dfs(i, idx - 1), presum[idx] - presum[i] + dfs(idx, j))
                right += 1
            for k in range(i, left):
                ans = max(ans, presum[k + 1] - presum[i] + dfs(i, k))
            for k in range(right, j + 1):
                ans = max(ans, presum[j + 1] - presum[k] + dfs(k, j))
            return ans
```
但是注意到如果搜索出现重复,遍历找最大值的时候遇到相同的(i,k)或者(k,j)，还是需要挨个比大小的(重复计算)
如果我们能保存一个区间内的左右搜索最大值,比如说`(i,left)`,那么我们搜索`(i,left+1)`的时候只需要比较(`presum[left+2]-presum[i] + dfs(i, left+1)`和之前的`(i,left)`谁更大即可)

实现方法就是使用记忆化递归代替循环求解最大值，从而保留不同区间的最大值

### 代码

```python3
class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            ans = 0
            half = (presum[j + 1] + presum[i]) / 2
            # 使用二分查找左右的大小中心位置
            idx = bisect.bisect_left(presum, half, lo=i, hi=j + 1)
            # idx 左边, left更小; idx 右边, right更小
            if presum[idx] == half:
                ans = max(ans, left_dfs(i, idx), right_dfs(idx, j))
            else:
                ans = max(ans, left_dfs(i, idx-1))
                ans = max(ans, right_dfs(idx, j))
            return ans

        @lru_cache(None)
        def left_dfs(i, j):
            if i >= j:
                return 0
            return max(presum[j] - presum[i] + dfs(i, j-1), left_dfs(i, j-1))

        @lru_cache(None)
        def right_dfs(i, j):
            if i >= j+1:
                return 0
            return max(presum[j+1] - presum[i] + dfs(i, j), right_dfs(i+1, j))

        presum = [0] + list(accumulate(stoneValue))
        return dfs(0, len(stoneValue) - 1)
```