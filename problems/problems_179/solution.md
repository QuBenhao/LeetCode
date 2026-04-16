# [Python] 自定义比较函数的排序

> Author: Benhao
> Date: 2021-04-12
> Upvotes: 1
> Tags: Python, Python3

---

### 解题思路
按两两下加后结果的大小排序

### 代码

```python
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int("".join(sorted(map(str, nums),key=cmp_to_key(lambda x,y:((x+y) < (y+x)) - ((x+y) > (y+x)))))))

```