# Python counter带记忆循环

> Author: Benhao
> Date: 2021-03-07
> Upvotes: 7
> Tags: Python

---

上一次分布中从i到j的counter可以用于计算从i到j+1的counter
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