# [From the archives] A concise version of an older solution

> slug: kao-gu-tie-ge-lao-ti-jie-de-jian-ji-ban-16mtv
> date: 2022-03-06
> tags: Python, Python3
> question: Base 7 (base-7)
> url: https://leetcode.cn/problems/base-7/solutions/qvRPKU/kao-gu-tie-ge-lao-ti-jie-de-jian-ji-ban-16mtv/

---
### Approach
[Repeated division for base conversion](https://leetcode.cn/problems/base-7/solution/pythonjavajavascriptgo-zhan-zhuan-xiang-752fe/)

### Code

```python3
class Solution:
    def convertToBase7(self, num: int) -> str:
        return ("-" if num < 0 else "") + self.convertToBase7(d) + str(a % 7) if (d := (a := abs(num)) // 7) > 0 else str(num)
```
