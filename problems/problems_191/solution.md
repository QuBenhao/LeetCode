# [Python] 用n&n-1 从右往左数1

> Author: Benhao
> Date: 2021-03-22
> Upvotes: 4
> Tags: Python

---

### 解题思路
n&n-1会消去最右边的1 
统计能消多少次即可
比如`101000`&`100111` = `100000`

### 代码

```python
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        while n:
            n &= n - 1
            ans += 1
        return ans

```