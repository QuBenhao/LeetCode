# [Python/Java/JavaScript/Go] 数学

> Author: Benhao
> Date: 2022-04-10
> Upvotes: 15
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
对于n位数，第一位有除0以外的9个数可选。
对于剩余数位，每次选前面没被选的，可选数从9依次递减。
当n大于0时，需要再叠加上第一位选0，相当于n-1位数的答案数。

### 代码

```Python3 []
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return 1 if not n else reduce(lambda x,y:x*y, [9] + [i for i in range(9, 10 - n, -1)]) + self.countNumbersWithUniqueDigits(n - 1)
```
```Java []
class Solution {
    public int countNumbersWithUniqueDigits(int n) {
        if(n == 0)
            return 1;
        int ans = 9;
        for(int i = 9; i > 10 - n; i--)
            ans *= i;
        return ans + countNumbersWithUniqueDigits(n - 1);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var countNumbersWithUniqueDigits = function(n) {
    if(n == 0)
        return 1
    let ans = 9
    for(let i = 9; i > 10 - n; i--)
        ans *= i
    return ans + countNumbersWithUniqueDigits(n - 1)
};
```
```Go []
func countNumbersWithUniqueDigits(n int) int {
    if n == 0 {
        return 1
    }
    ans := 9
    for i := 9; i > 10 - n; i-- {
        ans *= i
    }
    return ans + countNumbersWithUniqueDigits(n - 1)
}
```