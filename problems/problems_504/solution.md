# [考古] 贴个老题解的简洁版

> slug: kao-gu-tie-ge-lao-ti-jie-de-jian-ji-ban-16mtv
> date: 2022-03-06
> tags: Python, Python3
> question: Base 7 (base-7)
> url: https://leetcode.cn/problems/base-7/solutions/qvRPKU/kao-gu-tie-ge-lao-ti-jie-de-jian-ji-ban-16mtv/

---
### 解题思路
[辗转相除法解决所有进制转换问题](https://leetcode.cn/problems/base-7/solution/pythonjavajavascriptgo-zhan-zhuan-xiang-752fe/)

### 代码

```python3
class Solution:
    def convertToBase7(self, num: int) -> str:
        return ("-" if num < 0 else "") + self.convertToBase7(d) + str(a % 7) if (d := (a := abs(num)) // 7) > 0 else str(num)
```