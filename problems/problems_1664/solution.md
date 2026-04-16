# [Python] 奇偶前缀和

> Author: Benhao
> Date: 2021-05-29
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
删除的数左边奇偶性不变，右边奇偶性相反。统计奇偶前缀和可以o(1)求得任意位置删除后的和是否相等。

### 代码

```python3
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # 这题要求 奇数位和 和 偶数位和，在删除一个数以后，后面的奇偶性相反
        n = len(nums)
        odds = [0] * (n + 2)
        evens = [0] * (n + 2)
        for i,num in enumerate(nums):
            if i % 2 == 0:
                evens[i] = evens[i-2] + num
                odds[i] = odds[i-1]
            else:
                odds[i] = odds[i-2] + num
                evens[i] = evens[i-1]
        # print(evens, odds)
        ans = 0
        for i in range(n):
            # 新的奇数为i左边的奇数和 + i 右边的偶数和; 新的偶数相反
            if odds[i-1] + evens[n-1] - evens[i] == odds[n-1] - odds[i] + evens[i-1]:
                ans += 1
        return ans
```

看到利用正负区分奇偶的，学习了
```python3
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        # 偶数和与奇数和的差
        delta = sum(nums[0::2]) - sum(nums[1::2])
        # 符号
        flag = 1
        res = 0
        # 当前的和
        cur = 0
        for i, num in enumerate(nums):
            # 减去两倍前面的和可以使得符号颠倒（之前加的偶数和变为减，减的奇数和变为加）
            if delta - 2 * cur - flag * num == 0:
                res += 1
            cur += flag * num
            flag *= -1
        return res
```