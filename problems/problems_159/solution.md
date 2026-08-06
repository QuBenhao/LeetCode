# [Python] 模拟 o(n)

> slug: python-mo-ni-on-by-himymben-381l
> date: 2021-08-21
> tags: Python, Python3
> question: Longest Substring with At Most Two Distinct Characters (longest-substring-with-at-most-two-distinct-characters)
> url: https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/solutions/guUrtG/python-mo-ni-on-by-himymben-381l/

---
### 解题思路
好像加用例了效率比较低

### 代码

```python3
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = []
        window_index = defaultdict(int)
        ans = 0
        chars = set()
        for c in s:
            if len(chars) == 2 and c not in chars:
                other = (chars - {window[-1]}).pop()
                window = window[window_index[other] + 1:]
                chars.remove(other)
                window_index.pop(other)
                window_index[window[-1]] = len(window) - 1
            chars.add(c)
            window.append(c)
            window_index[c] = len(window) - 1
            ans = max(ans, len(window))
        return ans

```