# [Python] 前后缀堆

> Author: Benhao
> Date: 2022-02-06
> Upvotes: 2
> Tags: Python, Python3

---

### 解题思路
其实就是从中间n个数中找最优分割点，分割点左边n个数最小和和右边n个数最大和。

### 代码

```python3
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        pq = []
        l_sum = [0] * (2 * n)
        r_sum = [0] * (2 * n)
        for i in range(2 * n):
            num = nums[i]
            if len(pq) < n:
                heapq.heappush(pq, -num)
                l_sum[i] = l_sum[i - 1] + num
            elif num < -pq[0]:
                old = -heapq.heappop(pq)
                l_sum[i] = l_sum[i - 1] + num - old
                heapq.heappush(pq, -num)
            else:
                l_sum[i] = l_sum[i - 1]
        pq = []
        for i in range(2 * n):
            num = nums[-1-i]
            if len(pq) < n:
                heapq.heappush(pq, num)
                r_sum[-1-i] = r_sum[-i] + num
            elif num > pq[0]:
                old = heapq.heappop(pq)
                r_sum[-1-i] = r_sum[-i] + num - old
                heapq.heappush(pq, num)
            else:
                r_sum[-1-i] = r_sum[-i]
        return min(l_sum[n + i - 1] - r_sum[i] for i in range(n + 1))

```