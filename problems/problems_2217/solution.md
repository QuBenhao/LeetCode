# [Python] 脑筋急转弯

> slug: python-by-himymben-xxox
> date: 2022-03-27
> tags: Python, Python3
> question: Find Palindrome With Fixed Length (find-palindrome-with-fixed-length)
> url: https://leetcode.cn/problems/find-palindrome-with-fixed-length/solutions/hKiztW/python-by-himymben-xxox/

---
### 解题思路
脑筋急转弯，长度为intLength的第x个回文数是多少？

[1000][001]为长度为7的第一个回文数，那么第376个回文数为[1375][731]

### 代码

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