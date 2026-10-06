# [Python] 100% in both metrics: find the initial value with XOR

> Author: Benhao
> Date: 2021-05-10
> Upvotes: 2
> Tags: Python, Python3

---

### Approach
The XOR of perm[0] with each value in perm can be derived from encoded.
The XOR of every value in perm equals the XOR of 1 through n.
Since n is odd, XORing all the results of perm[0] XOR each value leaves the XOR of 1 through n excluding perm[0].
XOR these two results to obtain perm[0].

### Code

```python
class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        n = len(encoded) + 1
        # perm[0] = (perm[0] ^ perm[1] ^ ... perm[n-1]) ^ (perm[1] ^ perm[2]) ^ ... ^ (perm[n-2] ^ perm[n-1])
        # perm[0] = 1 ^ encoded[1] ^ encoded[3] ^ ... encoded[n-2] if n % 4 == 1 else encoded[1] ^ encoded[3] ^ ... encoded[n-2]
        start = 0
        for i in range(1, n, 2):
            start ^= encoded[i]
        # For odd n, the XOR of 1 through n is 1 when n mod 4 is 1, and 0 when it is 3
        if n % 4 == 1:
            start ^= 1
        perm = [start]
        for e in encoded:
            perm.append(perm[-1] ^ e)
        return perm
```
