# [Python] Applying prefix sums

> slug: python-qian-zhui-he-ying-yong-by-himymbe-dq0h
> date: 2022-04-24
> tags: Python, Python3
> question: Maximum Sum Score of Array (maximum-sum-score-of-array)
> url: https://leetcode.cn/problems/maximum-sum-score-of-array/solutions/NxAisk/python-qian-zhui-he-ying-yong-by-himymbe-dq0h/

---
### Approach
Solve by brute force with prefix sums.

### Code

```python3
class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        presum, n = [0] + list(accumulate(nums)), len(nums)
        return max(max(presum[i + 1], presum[n] - presum[i]) for i in range(n))
```
After computing the total sum, maintain the answer while traversing.
```python3
class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        p, s, ans = 0, sum(nums), -inf
        for num in nums:
            ans = max(ans, max(p + num, s - p))
            p += num
        return ans
```
