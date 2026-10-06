# [Python] Recursion

> slug: python-di-gui-by-himymben-zjk6
> date: 2021-08-22
> tags: Python, Python3
> question: Strobogrammatic Number II (strobogrammatic-number-ii)
> url: https://leetcode.cn/problems/strobogrammatic-number-ii/solutions/kssZN4/python-di-gui-by-himymben-zjk6/

---
### Approach
Add a symmetric pair to both ends each time, such as 6 on the left and 9 on the right.
Take care when inserting 0 in the middle: insert symmetric pairs, and do not allow 0 as the leading digit.

### Code

```python3
class Solution:
    reverseDict = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    @lru_cache(None)
    def findStrobogrammatic(self, n: int) -> List[str]:
        if not n:
            return ['']
        elif n == 1:
            return ['0', '1', '8']
        res = set()
        for ans in self.findStrobogrammatic(n-2):
            if n > 3:
                res.add('10'+ ans[1:-1] + '01')
                res.add('60' + ans[1:-1] + '09')
                res.add('80' + ans[1:-1] + '08')
                res.add('90' + ans[1:-1] + '06')
            res.add('6' + ans + '9')
            res.add('9' + ans + '6')
            res.add('1' + ans + '1')
            res.add('8' + ans + '8')
        return list(res)

```
