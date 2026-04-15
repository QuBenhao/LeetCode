# [Python] 爆搜

> Author: Benhao
> Date: 2022-10-30
> Upvotes: 14
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
按题意依次处理字母位

### 代码

```python3
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        for i, c in enumerate(s):
            if c.isalpha():
                ans = [a + c.lower() for a in ans] + [a + c.upper() for a in ans]
            else:
                ans = [a + c for a in ans]
        return ans
```