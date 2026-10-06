# [Python] Dynamic programming

> slug: python-dong-tai-gui-hua-by-himymben-frqm
> date: 2022-05-02
> tags: Python, Python3
> question: Substrings That Begin and End With the Same Letter (substrings-that-begin-and-end-with-the-same-letter)
> url: https://leetcode.cn/problems/substrings-that-begin-and-end-with-the-same-letter/solutions/nSQ34G/python-dong-tai-gui-hua-by-himymben-frqm/

---
### Approach
For each character, count the substrings that can end there: this is the number of occurrences of that character seen so far.

Alternatively, count all occurrences first and calculate the result together (the binomial coefficient $C_n2$).

### Code

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
