# [Python] 模拟

> Author: Benhao
> Date: 2022-10-23
> Upvotes: 6
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
根据题意直接模拟即可

### 代码

```python3
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(f"{a}{b}" for a, b in zip_longest(word1, word2, fillvalue=""))
```