# [Python] 递增三元组

> Author: Benhao
> Date: 2022-02-20
> Upvotes: 8
> Tags: Python, Python3

---

### 解题思路
将题目转换，用一个数组数字对应坐标的映射，去替换另一个数组。
这样做的目的是将题目转换为求一个数组中递增三元组的个数。
这是因为转换坐标映射，在第一个数组中的坐标大小必然是从小到大的，那么在第二个数组中的递增三元组自然而然满足了在第一个数组中的递增三元组这一条件。


转换后，和求最长递增子序列有一些相似。
比如用例一，从nums1可以得到映射如下: 2->0, 0->1, 1->2, 3->3，替换nums2得到[1,2,0,3]
我们要从nums2中统计递增三元组的个数，可以维护一个遍历过的值，快速统计当前值之前有多少个小于自己的数，想到单调栈结构。但是又因为在增加时不可以替换原栈的值，故使用SortedList


我们知道比当前值小的有idx个，当前走过的值有sl的长度个，可以很快统计出该点作为中间点的递增三元组个数为：$idx * (n - 1 - i - len(sl) + idx)$ 
【比$i$大的数有$n - 1 - i$个, 其中被走过了$len(sl) - idx$个】

### 代码

```python3
from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n, idx_map = len(nums1), {num:i for i, num in enumerate(nums1)}
        for i in range(n):
            nums2[i] = idx_map[nums2[i]]
        sl, ans = SortedList(), 0
        for i in nums2:
            idx = sl.bisect_left(i)
            ans += idx * (n - 1 - i - len(sl) + idx)
            sl.add(i)
        return ans
```