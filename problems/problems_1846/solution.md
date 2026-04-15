# [Python] 理解题目 o(nlogn) -> o(n)

> Author: Benhao
> Date: 2021-07-14
> Upvotes: 18
> Tags: Python, Python3

---

### 解题思路
第一个元素是1，第二个元素最多是2，第三个元素最多是3，以此类推，第n个元素最多是n。

但是由于每个数只能变成小于它的，不能变大，所以不是所有位置都能取到对应的值。
我们想要统计每个位置的取值，要用田忌赛马的感觉，排序以后，小的卡小的，大的卡大的，能不变小尽量不变小，看最后最多能取到多少。

### 代码

```python3
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        limit = 1
        for num in sorted(arr)[1:]:
            limit = min(limit + 1, num)
        return limit
```
不需要排序，维护一个记录1到n分别有多少个的数组即可。
Python因为遍历两遍，实际时间不一定比上面的快，但是时间复杂度确实更小
```python3
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnts = [0] * (n + 1)
        for num in arr:
            cnts[min(num, n)] += 1
        limit = 0
        for i in range(1, n + 1):
            limit = min(i, limit + cnts[i])
        return limit
```