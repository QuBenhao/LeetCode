# [Python] 同余定理 延迟添加前缀和变量

> Author: Benhao
> Date: 2021-06-02
> Upvotes: 42
> Tags: Python, Python3

---

### 解题思路
一开始看中等题很自然地想暴力解决，写下了如下代码：更新到当前数的所有和的余数，很自然地超时了。
```python3
        dp = set()
        temp = None
        for num in nums:
            if k - num % k in dp:
                return True
            dp = set((t + num) % k for t in dp)
            if temp is None:
                temp = num % k
            else:
                temp = (temp+num) % k
                if not temp:
                    return True
                dp.add(temp)
                temp = num % k
        return False
```

既然要求O(n)解法，那么必然不能像刚刚一样更新dp的所有余数。既然这题是连续子数组的和，必然是某种前缀和的差的关系。
假设我们想判断[i,j]的区间满足`(presum[j] - presum[i]) % k == 0`，那么显然要有`presum[j] % k == presum[i] % k`，本质就是同余定理。
又因为要求长度至少为2的子数组，所以我们需要记录从开始到现在的所有距离为2及以上的前缀和余数，
故使用`延时更新`(先判断有没有和当前前缀和同余的，再将上一个前缀和添加进set中)


### 代码

```python3
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        modes = set()
        presum = 0
        for num in nums:
            last = presum
            # 当前前缀和
            presum += num
            presum %= k
            # 同余定理
            if presum in modes:
                return True
            # 上一个前缀和，下一个就可以用了（距离为2了）
            modes.add(last)
        return False

```