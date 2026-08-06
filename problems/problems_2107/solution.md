# [Python] 滑动窗口

> slug: python-hua-dong-chuang-kou-by-himymben-v9tp
> date: 2022-05-01
> tags: Python, Python3
> question: Number of Unique Flavors After Sharing K Candies (number-of-unique-flavors-after-sharing-k-candies)
> url: https://leetcode.cn/problems/number-of-unique-flavors-after-sharing-k-candies/solutions/ohPsuP/python-hua-dong-chuang-kou-by-himymben-v9tp/

---
### 解题思路
定长滑窗模拟

### 代码

```python3
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        cnts = Counter(candies)
        for i in range(k):
            cnts[candies[i]] -= 1
            if not cnts[candies[i]]:
                del cnts[candies[i]]
        ans = len(cnts)
        for i in range(k, len(candies)):
            cnts[candies[i - k]] += 1
            cnts[candies[i]] -= 1
            if not cnts[candies[i]]:
                del cnts[candies[i]]
            ans = max(ans, len(cnts))
        return ans
```