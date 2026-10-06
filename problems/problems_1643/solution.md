# [Python] Combinatorics

> Author: Benhao
> Date: 2021-05-31
> Upvotes: 3
> Tags: Python, Python3

---

### Approach
I added comments to the reference implementation.
At each step, check whether choosing 'H' leaves at least k possible paths. If not, this position must be 'V'.

### Code

```python3
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        # Arrange h identical 'H' characters and v identical 'V' characters
        # Choose h positions for 'H' in a sequence of length h+v
        # Thus, h and v give comb(h+v,h) combinations
        v, h = destination 
        res = ''
        while h > 0 and v > 0:
            # Paths starting with 'H' precede those starting with 'V'; choosing 'H' reduces h by 1 and leaves v unchanged
            # Number of combinations with 'H' here
            num = math.comb(h + v - 1, h - 1)
            # If choosing 'H' gives fewer than k paths, choose V and find path k-num among the remaining paths
            if k > num:
                res += 'V'
                v -= 1
                k -= num 
            # Otherwise, choose 'H' and continue deciding between 'H' and 'V'
            else:
                res += 'H'
                h -= 1
        # At a boundary, only one path remains: go straight to the destination
        return res + h * 'H' + v * 'V'
```
