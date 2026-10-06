# [Python] Make-nine game

> Author: Benhao
> Date: 2021-07-11
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
Bob can guarantee a win despite Alice's choices only by always completing pairs to 9. The initial difference must be a multiple of 9, with enough remaining moves on both sides to make up the difference.

### Code

```python
class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        s = a = b = 0
        n = len(num)
        for i,c in enumerate(num):
            if i < n // 2:
                if c == '?':
                    a += 1
                else:
                    s += int(c)
            else:
                if c == '?':
                    b += 1
                else:
                    s -= int(c)
        # Alice moves first and can keep the difference from being a multiple of 9, leaving unequal final sums
        if (a + b) % 2 == 1:
            return True
        # With equal move counts, Bob wins when the difference can be made up by completing pairs to multiples of 9
        if s % 9 == 0 and s // 9 == b - a >> 1:
            return False
        return True
```
