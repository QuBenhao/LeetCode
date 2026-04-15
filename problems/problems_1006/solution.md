# [Python] 从直接的解法到数学推算简化

> Author: Benhao
> Date: 2021-04-01
> Upvotes: 1
> Tags: Python

---

### 解题思路
一开始很直接的思路: 只有第一个乘除运算是被加的，后面的所有乘除运算都是被减的。
后面又因为乘除是很接近的数，不难发现他们的结果的规律。
`n * (n-1) / (n-2) = (n^2 - n) / (n-2) = (n^2 - 2n + n - 2 + 2) / (n-2) = n + 1 + 2 / (n - 2) = n + 1`, 只有当`n-2>2`,即`n>4`时，这个式子才成立。
于是我们有:
```
clumsy(n) = n * (n-1) // (n-2) + (n-3) - (n-4) * (n-5) // (n-6) + (n-7) - (n-8) * (n-9) // (n-10) + ...
          = (n+1) + (n-3) - (n-3) + (n-7) - (n-7) + ...
          = (n+1) + ...
```
根据这一推算，可以省去很多不必要的运算。

### 代码

```python
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N > 4:
            ans = N * (N-1) // (N-2) + (N-3)
            N -= 4
        elif N == 4:
            return 7
        elif N == 3:
            return 6
        else:
            return N

        while N > 4:
            ans -= N * (N-1) // (N-2) - (N-3)
            N -= 4

        if N == 4:
            ans -= N * (N-1) // (N-2) - (N-3)
        elif N == 3:
            ans -= N * (N-1) // (N-2)
        elif N == 2:
            ans -= N * (N-1)
        else:
            ans -= N
        return ans
```

```python
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        clumsy(n) = n * (n-1) // (n-2) + (n-3) - (n-4) * (n-5) // (n-6) + (n-7) - (n-8) * (n-9) // (n-10) + ...
                  = (n+1) + (n-3) - (n-3) + (n-7) - (n-7) + ...
                  = (n+1) + ...
        """
        if N > 4:
            # 后面全部抵消
            if N % 4 == 0:
                return N + 1
            # 最后一个 2 // (N-2) 要多出一个 - 2来, 所以是 N + 1 - 2
            elif N % 4 == 3:
                return N - 1
            # 1 的时候最后剩下一个 + 2 - 1 = 1
            # 2 的时候最后剩下一个 + 3 - 2 * 1 = 1
            # 所以 N + 1 + 1
            else:
                return N + 2
        elif N == 4:
            return 7
        elif N == 3:
            return 6
        else:
            return N
```

上面代码的另一种简化写法就是：
```python
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        clumsy(n) = n * (n-1) // (n-2) + (n-3) - (n-4) * (n-5) // (n-6) + (n-7) - (n-8) * (n-9) // (n-10) + ...
                  = (n+1) + (n-3) - (n-3) + (n-7) - (n-7) + ...
                  = (n+1) + ...
        """
        return [0, 1, 2, 6, 7][N] if N < 5 else N + [1, 2, 2, -1][N%4]
```