# [Python] Recurrence

> Author: Benhao
> Date: 2021-03-02
> Upvotes: 1
> Tags: Python

---

Notice that the range starts at 0 and ends at n:
Initially, the array is [0] for the number 0.
For the first bit, append 0+1, producing [0,1] for the number 1.
For the second bit, append 0+1 and 1+1, producing [0, 1, 1, 2] for the numbers 2 and 3.
For the third bit, append 0+1, 1+1, 1+1, and 2+1, producing [0, 1, 1, 2, 1, 2, 2, 3] for the numbers 4, 5, 6, and 7.
Continue in the same way up to n.

```
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        curr = 0
        ans = [0]
        while curr < num:
            new = []
            for i in ans:
                if curr == num:
                    return ans + new
                new.append(1+i)
                curr += 1
            ans += new
        return ans
```
