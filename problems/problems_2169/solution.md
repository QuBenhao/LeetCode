# [Python/Go] 辗转相除

> Author: Benhao
> Date: 2022-02-13
> Upvotes: 1
> Tags: Go, Python, Python3

---

### 解题思路
当一个数比另一个数大很多时，我们会发现需要大数减小数的倍数次（大数除小数）
减到最后大数变成除小数的余数，小数变成了更大的那个数

### 代码

```Python3 []
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        while num1:
            ans += num2 // num1
            num1, num2 = num2 % num1, num1
        return ans
```
```Go []
func countOperations(num1 int, num2 int) (ans int) {
    for num1 > 0 {
        ans += num2/num1
        num1, num2 = num2 % num1, num1
    }
    return
}
```