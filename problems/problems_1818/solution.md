# [Python] 模拟 排序后二分

> Author: Benhao
> Date: 2021-07-13
> Upvotes: 33
> Tags: Python, Python3

---

### 解题思路
其实就是找每个nums2中的值，对应在nums1中最接近的值是哪个，替换为那一个以后的绝对值和是多少；统计最终最小的即可。

>具体来说:
我们先统计一下原始的绝对值差的和，如果已经为0可以直接返回，不为0我们开始遍历每个位置，找对应位置的最佳替换元素(二分)，计算替换后的新的绝对值差的和，更新最小的到答案。

### 代码

```python3
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        diff = sum(abs(nums1[i] - nums2[i]) for i in range(n))
        if not diff:
            return 0
        ans = inf
        sl = sorted(nums1)
        for i, num in enumerate(nums2):
            idx = bisect.bisect_left(sl, num)
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, diff - abs(nums1[i] - nums2[i]) + abs(sl[idx-1] - nums2[i]))
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, diff - abs(nums1[i] - nums2[i]) + abs(sl[idx] - nums2[i]))
        return ans % (10 ** 9 + 7)
```
因为上面我们总是比较了全部的diff在运算中，其实是不需要的，单独统计加入最终答案即可。写成一个单循环的解法如下:
```python3
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n, total, sl, ans = len(nums1), 0, sorted(nums1), inf
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            total += diff
            idx = bisect.bisect_left(sl, nums2[i])
            # idx > 0 尝试用idx-1替换当前值
            if idx:
                ans = min(ans, abs(sl[idx-1] - nums2[i]) - diff)
            # idx < n 尝试用idx替换当前值
            if idx < n:
                ans = min(ans, abs(sl[idx] - nums2[i]) - diff)
        return (total + ans) % (10 ** 9 + 7) if total else total
```