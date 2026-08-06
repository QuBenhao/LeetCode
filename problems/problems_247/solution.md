# [Python] 递归

> slug: python-di-gui-by-himymben-zjk6
> date: 2021-08-22
> tags: Python, Python3
> question: Strobogrammatic Number II (strobogrammatic-number-ii)
> url: https://leetcode.cn/problems/strobogrammatic-number-ii/solutions/kssZN4/python-di-gui-by-himymben-zjk6/

---
### 解题思路
每次往两边叠加对称数，比如左边+6，右边+9；
要额外注意0在中间的加入方式，需要两位对称(0不能作为首字母)

### 代码

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