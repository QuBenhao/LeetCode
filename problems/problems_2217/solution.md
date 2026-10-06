# [Python] Brain teaser

> slug: python-by-himymben-xxox
> date: 2022-03-27
> tags: Python, Python3
> question: Find Palindrome With Fixed Length (find-palindrome-with-fixed-length)
> url: https://leetcode.cn/problems/find-palindrome-with-fixed-length/solutions/hKiztW/python-by-himymben-xxox/

---
### Approach
A brain teaser: what is the x-th palindrome of length intLength?

[1000][001] is the first palindrome of length 7, so the 376th is [1375][731].

### Code

```python3
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        idx_map = defaultdict(list)
        ans = [-1] * len(queries)
        for i, q in enumerate(queries):
            idx_map[q].append(i)
        base = 10 ** ((intLength-1) // 2)
        mx = 10 ** ((intLength-1) // 2 + 1) - base
        for q in sorted(queries):
            if q > mx:
                break
            s = str(base + q - 1)
            res = s + s[::-1] if not intLength % 2 else s[:-1] + s[-1] +s[:-1][::-1]
            r = int(res)
            for idx in idx_map[q]:
                ans[idx] = r
        return ans
```
