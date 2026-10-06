# [Python] Without an iterator

> slug: python-mei-yong-die-dai-qi-by-himymben-w7e3
> date: 2021-08-22
> tags: Python, Python3
> question: Flatten 2D Vector (flatten-2d-vector)
> url: https://leetcode.cn/problems/flatten-2d-vector/solutions/bobg8x/python-mei-yong-die-dai-qi-by-himymben-w7e3/

---
### Approach
I should have used Java for this. Check whether the current list has another value; if not, check whether the outer list has another list.

### Code

```python3
class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.list = [num for nums in vec for num in nums]
        self.idx = 0

    def next(self) -> int:
        val = self.list[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.list)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```
