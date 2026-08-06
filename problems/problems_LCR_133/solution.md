# [Python] 又回到了位运算

> slug: python-you-hui-dao-liao-wei-yun-suan-by-d8m8u
> date: 2021-06-22
> tags: Python, Python3
> question: 位 1 的个数 (er-jin-zhi-zhong-1de-ge-shu-lcof)
> url: https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solutions/Ylq2XJ/python-you-hui-dao-liao-wei-yun-suan-by-d8m8u/

---
### 解题思路
如代码

### 代码

```python3
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count('1')
        
        ans = 0
        while n:
            n -= n & -n
            ans += 1
        return ans
```