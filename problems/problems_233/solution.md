# [Python/Java] Recursive solution

> slug: python-di-gui-qiu-jie-by-qubenhao-a3lc
> date: 2021-08-13
> tags: Java, Python, Python3
> question: Number of Digit One (number-of-digit-one)
> url: https://leetcode.cn/problems/number-of-digit-one/solutions/BQai4x/python-di-gui-qiu-jie-by-qubenhao-a3lc/

---
### Approach
> First, observe this pattern:
> Up to 9, there is `1` occurrence of the digit 1.
> Up to 99, the ones digits contribute 1 from each of ten groups of 0-9, and the tens digits contribute 1 for 10-19, giving 10 + 10*1 = `20`.
> Up to 999, there are 100 + 10 * 20 = `300` occurrences.
> And so on


Given n, first determine how many complete blocks ending in 9999.. it contains. For example, `3278` contains three such blocks, ending at 0999, 1999, and 2999. This gives the res component: the number of 1s in `999` multiplied by the leading digit. Two contributions remain: 1s in the lower digits when the leading digit is 3, and all occurrences of 1 in the leading position.

The first contribution is a recursive subproblem: for `3278`, count the 1s in `278`, which gives the lower-digit contribution when the leading digit is `3`. For the second, check whether the leading digit exceeds 1. `3278` includes every leading 1 in `1000-1999`, whereas `1278` includes only 279 leading 1s. Add the appropriate count when returning.

> Note: The leading digit of n cannot be 0, so it is either 1 or greater than 1.

### Code

```Python3 []
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 10:
            return 1 if n else 0
        num = str(n)
        x = len(num) - 1
        nxt = int(num[1:])
        res = self.f(x) * int(num[0]) + self.countDigitOne(nxt)
        # If the leading digit exceeds 1, it contributes 10**x ones; otherwise, use the remaining part of num plus the one in "10000.."
        return res + 10 ** x if int(num[0]) > 1 else res + nxt + 1

    """
    0-9: 1
    0-99: 10 + 10 * 1 = 20
    0-999: 100 + 10 * 20 = 300
    0-9999: 1000 + 10 * 300 = 4000
    0-99999: 10000 + 10 * 4000 = 50000
    f(i) = 10 ** (i-1) + 10 * f(i-1)
    Alternatively, write f(i) = i * 10 ** (i-1) directly.
    """
    @lru_cache(None)
    def f(self, i):
        # return i * 10 ** (i-1)
        return 10 ** (i-1) + 10 * self.f(i-1) if i else 0
```
```Java []
class Solution {
    // dp[i] = i * (int)Math.pow(10, i-1);
    int[] dp = new int[]{0,1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000};
    public int countDigitOne(int n) {
        if(n < 10)
            return n == 0 ? 0 : 1;
        String num = String.valueOf(n);
        int length = num.length() - 1, first = num.charAt(0) - '0';
        int firstNum = (int)Math.pow(10, length);
        int nxt = n - firstNum * first;
        return first > 1 ? countDigitOne(nxt) + dp[length] * first + firstNum : countDigitOne(nxt) + dp[length] * first + nxt + 1;
    }
}
```

### Complexity
Analysis: Each recursive call processes and removes the leftmost digit. The number shrinks by roughly a factor of 10, with at least one fewer digit in the next call. Therefore:
Time complexity $o(log_{10}n)$
Space complexity $o(log_{10}n)$
More precisely, the bound is the number of nonzero digits in n.
