# [Python] 暴力

> slug: python-bao-li-by-himymben-z05r
> date: 2021-08-22
> tags: Python, Python3
> question: Reverse Words in a String II (reverse-words-in-a-string-ii)
> url: https://leetcode.cn/problems/reverse-words-in-a-string-ii/solutions/MTh53h/python-bao-li-by-himymben-z05r/

---
```python3
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        res = ' '.join(''.join(s).split(' ')[::-1])
        for i in range(len(s)):
            s[i] = res[i]
```