# [Python/Java] Bit manipulation with recursion or iteration

> slug: pythonjava-wei-yun-suan-di-gui-or-die-da-7esn
> date: 2021-09-25
> tags: Java, Python, Python3
> question: Sum of Two Integers (sum-of-two-integers)
> url: https://leetcode.cn/problems/sum-of-two-integers/solutions/f3CDOE/pythonjava-wei-yun-suan-di-gui-or-die-da-7esn/

---
### Approach
See the Python comments for the reasoning.

XOR directly computes the sum when a&b is 0, because 0101 + 1010 = 1111 = 0101 ^ 1010.
When a&b is nonzero, XOR sets the corresponding bits to 0, but adding two 1s requires a carry. Thus, (a&b)<<1 obtains all carry bits. XOR again and repeat until no carry remains.

### Code
```Python3 []
MAX = 1024
MAX_INT = 1023
class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        a 001
        b 010
        a^b 011
        -------
        a 010
        b 011
        a^b 001
        ===> Collect all carry bits
        a^b^((a&b)<<1)
        -------
        a 010100
        b 011110
        a^b 001010
        All carry bits: 101010
        XOR with the carry bits may generate further carries!
        Therefore, use a loop or iteration.
        -------
        Negative two's-complement values keep supplying a leading 1; handle negative values specially using bitwise inversion.
        Python needs explicit integer overflow handling.
        Since the input range is 1000, take 1024-1 as the maximum integer and handle overflow at that boundary.
        """
        def int_overflow(val):
            if not -MAX <= val <= MAX_INT:
                val = (val + MAX) % (2 * MAX) - MAX
            return val
        while b:
            a,b = int_overflow(a^b), int_overflow((a & b) << 1)
        return a
```
```Java []
class Solution {
    public int getSum(int a, int b) {
        return b == 0 ? a : getSum(a ^ b, (a & b) << 1);
    }
}
```
