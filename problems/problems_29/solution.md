# [Python/Java/JavaScript] Trial division by subtraction 

> Author: Benhao
> Date: 2021-10-11
> Upvotes: 85
> Tags: Java, JavaScript, Python, Python3

---

### Approach
Use $2^i$ as the multiplier: $x * 2^i = x << i$.
Try powers from $2^{31}$ down to $2^0$ until subtraction reduces the dividend below the divisor,
adding each largest valid power of 2 to the answer.
This can also be viewed as calculating one of the answer's 32 bits at each step.

### Code

```Python3 []
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a; in other words, a/b = 2^i + (a-2^i*b)/b
            if (b << i) <= a:
                res += 1 << i
                a -= b << i
        return res if (dividend > 0) == (divisor > 0) else -res
```
```Java []
class Solution {
    public int divide(int dividend, int divisor) {
        if(dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        long a = Math.abs((long)dividend), b = Math.abs((long)divisor);
        int res = 0;
        for(int i=31;i>=0;i--){
            if((a>>i)>=b){
                res += 1 << i;
                a -= b<<i;
            }
        }
        return (dividend > 0) == (divisor > 0) ? res : -res;
    }
}
```
```JavaScript []
/**
 * @param {number} dividend
 * @param {number} divisor
 * @return {number}
 */
const MAX = 2147483647, MIN = -2147483648;
var divide = function(dividend, divisor) {
    if(dividend == MIN && divisor == -1)
        return MAX;
    let a = Math.abs(dividend), b = Math.abs(divisor), res = 0;
    for(let i=31;i>=0;i--){
        if((a>>>i)>=b){
            // 1<<31 = -2147483648, which requires special handling
            if(i==31){
                a -= MAX;
                a -= 1;
                res -= MIN;
            } else{
                a -= b<<i;
                res += 1<<i;
            }
        }
    }
    return (dividend > 0) == (divisor > 0) ? res : -res;
};
```
