# [Python] Greedy with two pointers

> slug: python-tan-xin-shuang-zhi-zhen-xie-fa-by-yr3g
> date: 2022-02-20
> tags: Python, Python3
> question: Construct String With Repeat Limit (construct-string-with-repeat-limit)
> url: https://leetcode.cn/problems/construct-string-with-repeat-limit/solutions/8kVXo4/python-tan-xin-shuang-zhi-zhen-xie-fa-by-yr3g/

---
### Approach
Prefer the largest character. When it cannot be added again, use the next-largest character (if more of the current largest remain, add just one smaller character before returning to it).

### Code

```python3
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        def build(i):
            le = min(repeatLimit, cnts[keys[i]])
            if not le:
                return i + 1
            ans.append(keys[i] * le)
            cnts[keys[i]] -= le
            while i < len(keys) and not cnts[keys[i]]:
                i += 1
            return i

        ans, cnts = [], Counter(s)
        keys = sorted(cnts.keys(), reverse=True)
        i, j = 0, 1
        while i < len(keys):
            if j == i:
                j += 1
            if ans and ans[-1][0] == keys[i]:
                if j < len(keys):
                    cnts[keys[j]] -= 1
                    ans.append(keys[j])
                    while j < len(keys) and not cnts[keys[j]]:
                        j += 1
                    i = build(i)
                else:
                    break
            else:
                i = build(i)
        return "".join(ans)

```
