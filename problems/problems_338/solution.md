# [Python] 递推解法

> Author: Benhao
> Date: 2021-03-02
> Upvotes: 1
> Tags: Python

---

注意到是从0到n的:
一开始数组是[0] --- 0 的时候
到第一位的时候添加了0+1，数组变为[0,1] --- 1 的时候
到第二位的时候添加了0+1 和 1+1， 数组变为 [0, 1, 1, 2] --- 2 和 3 的时候
到第三位的时候添加了0+1，1+1，1+1 和 2+1， 数组变为 [0, 1, 1, 2, 1, 2, 2, 3] --- 4, 5, 6, 7 的时候
以此类推直到n即可

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