# [Python] 今天这题太难了我真不会

> slug: python-jin-tian-zhe-ti-tai-nan-liao-wo-z-6wbs
> date: 2021-12-22
> tags: Python, Python3
> question: Longest Duplicate Substring (longest-duplicate-substring)
> url: https://leetcode.cn/problems/longest-duplicate-substring/solutions/FXznWC/python-jin-tian-zhe-ti-tai-nan-liao-wo-z-6wbs/

---
### 解题思路
我废了，只会这样比较暴力的混一混了…具体值得学习的算法还是参考叶总、可乐总、烟花佬、dian神等诸位大佬的代码吧。

### 代码

```python3
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            while s[i:i+len(ans)+1] in s[i+1:]:
                ans = s[i:i+len(ans) + 1]
        return ans
```