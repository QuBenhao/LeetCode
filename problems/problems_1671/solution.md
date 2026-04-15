# [Python] LIS 正反向最长递增子序列

> Author: Benhao
> Date: 2021-05-26
> Upvotes: 3
> Tags: Python, Python3

---

### 解题思路
题目是山形数组，要找到左边一串递增，右边一串递减，且删除次数尽可能少。
那么我们循环考虑每个点作为山顶时，我们要怎么统计删除次数呢？
换句话说，如果有一个点作为山顶，它的左边最少要删除几次？右边最少要删除几次呢？
再换句话说，以一个点作为最大值的最长递增子序列是多长呢？

### 代码

```python3
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # 从左到右的最长递增序列
        forward = self.LIS(nums)
        # 从右到左的最长递增序列
        backward = self.LIS(nums[::-1])[::-1]
        res = 0
        for i in range(n):
            # 山顶的点不能在两侧，两边至少有额外的一个比自己小的点
            if forward[i] > 1 and backward[i] > 1:
                # 左右构成的最长山形数组 由两者的和的决定 （去掉当前的重复1）
                res = max(res, forward[i] + backward[i] - 1)
        return n - res
    
    def LIS(self, nums):
        n = len(nums)
        dp = [1] * n
        curr = [nums[0]]
        for i in range(1, n):
            # 找到nums[i]在curr中的位置
            idx = bisect.bisect_left(curr, nums[i])
            # 如果idx最大，加入最长递增子序列中
            if idx == len(curr):
                curr.append(nums[i])
            # 否则替换其所在位置的curr[idx]
            else:
                curr[idx] = nums[i]
            # nums[i] 能取到的最长递增子序列就是idx+1
            dp[i] = idx + 1
        return dp

```