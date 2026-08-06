# [Python/Java/JavaScript/Go] 数学

> slug: pythonjavajavascriptgo-shu-xue-by-himymb-9nkj
> date: 2022-03-02
> tags: Go, Java, JavaScript, Python, Python3
> question: Add Digits (add-digits)
> url: https://leetcode.cn/problems/add-digits/solutions/J6sgQd/pythonjavajavascriptgo-shu-xue-by-himymb-9nkj/

---
### 解题思路
观察:
1. 最终答案肯定为0-9
2. 只有0才能得到0，其他数字只要有数就永远不会加出0，那么其他数字只能对应1-9
3. 函数满足 f(a + 1) = f(a) + 1 (这里结果的10看作1)

结果只能是1-9的无限循环

9个一循环，也就是f(a + 9) = f(a)，那么我们抛去加的多余的9，结果一致，即f(a) = f(a % 9) (这里结果的f(0)看作9)

### 代码

```Python3 []
class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1 if num else num
```
```Java []
class Solution {
    public int addDigits(int num) {
        return num == 0 ? num : (num - 1) % 9 + 1;
    }
}
```
```JavaScript []
/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    return num == 0 ? num : (num - 1) % 9 + 1
};
```
```Go []
func addDigits(num int) int {
    if num == 0 {
        return num
    } else {
        return (num - 1) % 9 + 1
    }
}
```