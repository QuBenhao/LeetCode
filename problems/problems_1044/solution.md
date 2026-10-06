# [Python] Today's problem is too hard for me

> slug: python-jin-tian-zhe-ti-tai-nan-liao-wo-z-6wbs
> date: 2021-12-22
> tags: Python, Python3
> question: Longest Duplicate Substring (longest-duplicate-substring)
> url: https://leetcode.cn/problems/longest-duplicate-substring/solutions/FXznWC/python-jin-tian-zhe-ti-tai-nan-liao-wo-z-6wbs/

---
### Approach
I'm stuck; this fairly brute-force approach is all I can manage... For algorithms worth studying, refer to the code from 叶总, 可乐总, 烟花佬, dian神, and the other experts.

### Code

```python3
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            while s[i:i+len(ans)+1] in s[i+1:]:
                ans = s[i:i+len(ans) + 1]
        return ans
```
