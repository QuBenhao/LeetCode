# [Python/Java/JavaScript] 减法试除 

> Author: Benhao
> Date: 2021-10-11
> Upvotes: 85
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
用$2^i$去作为乘法基数, $x * 2^i = x << i$。
从$2^{31}$试到$2^0$直到被除数被减到比除数小，
每个能满足除出来的最大的2的幂都加入答案
也可以理解为每次计算出答案的32位中的某一位

### 代码

```Python3 []
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 2^i * b <= a 换句话说 a/b = 2^i + (a-2^i*b)/b
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
            // 1<<31 = -2147483648，需特殊处理
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