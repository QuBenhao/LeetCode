# [Python] 贪心-双指针写法

> slug: python-tan-xin-shuang-zhi-zhen-xie-fa-by-yr3g
> date: 2022-02-20
> tags: Python, Python3
> question: Construct String With Repeat Limit (construct-string-with-repeat-limit)
> url: https://leetcode.cn/problems/construct-string-with-repeat-limit/solutions/8kVXo4/python-tan-xin-shuang-zhi-zhen-xie-fa-by-yr3g/

---
### 解题思路
优先加大的字母，加不了了加下一个大的字母（如果还有当前大字母就先加一个下一个再继续加当前字母）

### 代码

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