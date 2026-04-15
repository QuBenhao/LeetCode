# [Python] 模拟

> Author: Benhao
> Date: 2022-10-29
> Upvotes: 3
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
模拟

### 代码

```python3
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum((ruleKey == "type" and t == ruleValue) or (ruleKey == "color" and c == ruleValue) or (ruleKey == "name" and n == ruleValue) for t, c, n in items)
```
```Python3
KEYS = ["type", "color", "name"]
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(ruleValue == item[idx] for item in items) if (idx := KEYS.index(ruleKey)) >= 0 else 0
```