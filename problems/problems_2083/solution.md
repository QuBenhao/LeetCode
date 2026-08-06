# [Python] 动态规划

> slug: python-dong-tai-gui-hua-by-himymben-frqm
> date: 2022-05-02
> tags: Python, Python3
> question: Substrings That Begin and End With the Same Letter (substrings-that-begin-and-end-with-the-same-letter)
> url: https://leetcode.cn/problems/substrings-that-begin-and-end-with-the-same-letter/solutions/nSQ34G/python-dong-tai-gui-hua-by-himymben-frqm/

---
### 解题思路
遍历每个字母可以作为结尾的子串个数，实际上是前面该字符出现的次数。

也可以直接统计所有次数，一起计算。(组合数$C_n2$)

### 代码

```python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnts, ans = [0] * 26, 0
        for c in s:
            cnts[ord(c) - ord('a')] += 1
            ans += cnts[ord(c) - ord('a')]
        return ans
```
```python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return sum(v * (v + 1) >> 1 for v in Counter(s).values())
```