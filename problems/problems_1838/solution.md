# [Python] 滑动窗口

> Author: Benhao
> Date: 2021-07-19
> Upvotes: 11
> Tags: Python, Python3

---

### 解题思路
排序后，对于每个滑动窗口的右端点j，我们要找尽可能靠左的i，使得k足够把之间所有的数都加到nums[j]。
换句话说，`nums[j] * (j - i + 1) <= k + nums[i] + nums[i+1] + ... + nums[j-1] + nums[j]`，对于每个`j`我们要找满足这个最小的那个`i`。
所以在代码中，我们总是加入右端点的值，如果上式成立，该窗口的大小就是可以作为答案的，如果不行，我们要移动窗口左端点`i`(if和while的区别见下)
<br>
为什么是`if`不是`while`，只移动一次？
如果当前i，j不满足这个式子了，我们就移动一下最左边的指针即可，这样可以保证它和上一次的窗口大小一致（如果我们遇到了最长的窗口，后面的窗口和可能始终不满足，但是答案的大小固定，我们想寻找有没有更长的窗口而已)
如果要改成while，需要使用一个变量纪录最大的答案

### 代码

用if
```python3
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = j = 0
        # 问题转化一下，排序后 nums[j] * (j - i + 1) <= k + presum[j + 1] - presum[i]
        for j, num in enumerate(nums):
            k += num
            if k < num * (j - i + 1):
                k -= nums[i]
                i += 1
            # 当前滑窗不一定满足该式子，但一定存在满足该i,j距离的滑窗
        return j - i + 1
```
用while
```python3
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = ans = 0
        # 问题转化一下，排序后 nums[j] * (j - i + 1) <= k + presum[j + 1] - presum[i]
        for j, num in enumerate(nums):
            k += num
            while k < num * (j - i + 1):
                k -= nums[i]
                i += 1
            # 对于当前j最远的i
            ans = max(ans, j - i + 1)
        return ans
```