# [Python] From a direct solution to a mathematical simplification

> Author: Benhao
> Date: 2021-04-01
> Upvotes: 1
> Tags: Python

---

### Approach
The initial idea is straightforward: only the first multiplication/division group is added; all later multiplication/division groups are subtracted.
Since the numbers in each multiplication/division group are close together, a pattern in their results is easy to find.
`n * (n-1) / (n-2) = (n^2 - n) / (n-2) = (n^2 - 2n + n - 2 + 2) / (n-2) = n + 1 + 2 / (n - 2) = n + 1` holds only when `n-2>2`, that is, `n>4`.
This gives:
```
clumsy(n) = n * (n-1) // (n-2) + (n-3) - (n-4) * (n-5) // (n-6) + (n-7) - (n-8) * (n-9) // (n-10) + ...
          = (n+1) + (n-3) - (n-3) + (n-7) - (n-7) + ...
          = (n+1) + ...
```
This derivation eliminates many unnecessary calculations.

### Code

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
            # All subsequent terms cancel
            if N % 4 == 0:
                return N + 1
            # The final 2 // (N-2) contributes an extra - 2, giving N + 1 - 2
            elif N % 4 == 3:
                return N - 1
            # For remainder 1, the final terms are + 2 - 1 = 1
            # For remainder 2, the final terms are + 3 - 2 * 1 = 1
            # Therefore, N + 1 + 1
            else:
                return N + 2
        elif N == 4:
            return 7
        elif N == 3:
            return 6
        else:
            return N
```

Another simplified version of the code above is:
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
