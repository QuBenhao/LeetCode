# [Python] 模拟

> Author: Benhao
> Date: 2024-03-13
> Upvotes: 10
> Tags: C, Go, Java, Python3, TypeScript

---

### 解题思路
从右往左模拟加一看进位即可

### 代码

```python3
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = 1
        for i in range(len(digits) - 1, -1, -1):
            cur += digits[i]
            digits[i] = cur % 10
            cur //= 10
        return digits if not cur else [cur] + digits

```