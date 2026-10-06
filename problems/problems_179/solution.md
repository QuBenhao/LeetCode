# [Python] Sort with a custom comparison function

> Author: Benhao
> Date: 2021-04-12
> Upvotes: 1
> Tags: Python, Python3

---

### Approach
Sort by comparing the results of concatenating each pair in both orders.

### Code

```python
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return str(int("".join(sorted(map(str, nums),key=cmp_to_key(lambda x,y:((x+y) < (y+x)) - ((x+y) > (y+x)))))))

```
