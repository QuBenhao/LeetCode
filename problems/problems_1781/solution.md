# Python Counter with incremental reuse

> Author: Benhao
> Date: 2021-03-07
> Upvotes: 7
> Tags: Python

---

Reuse the Counter for i through j to compute the Counter for i through j+1.
```
    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        li = []
        for c in s:
            new = [0] * 26
            i = ord(c) - ord('a')
            new[i] = 1
            for counter in li:
                counter[i] += 1
                ans += max(counter) - min(k for k in counter if k)
            li.append(new)
        return ans
```
