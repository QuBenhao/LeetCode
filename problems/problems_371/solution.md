# [Python/Java] 位运算 递归 or 迭代

> slug: pythonjava-wei-yun-suan-di-gui-or-die-da-7esn
> date: 2021-09-25
> tags: Java, Python, Python3
> question: Sum of Two Integers (sum-of-two-integers)
> url: https://leetcode.cn/problems/sum-of-two-integers/solutions/f3CDOE/pythonjava-wei-yun-suan-di-gui-or-die-da-7esn/

---
### 解题思路
思路过程看我Python里的注释

我们用异或可以直接求得a&b为0的加法。这是因为 0101 + 1010 = 1111 = 0101 ^ 1010
当a&b不为0时，对应位异或结果变为0，但是相当于两个1加在一起要进位，所以(a&b)<<1求得所有进位的1，再进行异或，直到不存在进位为止。

### 代码
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
        ===> 统计所有进位的1
        a^b^((a&b)<<1)
        -------
        a 010100
        b 011110
        a^b 001010
        所有进位 101010
        进位的异或还可能有进位!
        所以要使用循环or迭代处理
        -------
        负数补码总会提供最左的1，按位取反，要特殊处理负数
        Python需要要做整数的溢出
        既然数据范围是1000，那我们认定最大的整数是1024-1做溢出即可
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