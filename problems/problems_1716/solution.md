# [Python/Java/JavaScript/Go] 数学 简单题困难做

> Author: Benhao
> Date: 2022-01-14
> Upvotes: 28
> Tags: Math, C, Go, Java, JavaScript, Python, Python3

---

### 解题思路
根据题意推导数学公式

### 代码

```Python3 []
class Solution:
    def totalMoney(self, n: int) -> int:
        return (div:=n//7) * (1 + 7) * 7 // 2 + (m:=max(div - 1, 0)) * (m + 1) * 7 // 2 +  (1 + (r:=n%7)) * r // 2 + div * r
```
```Java []
class Solution {
    public int totalMoney(int n) {
        int div = n / 7, r = n % 7, m = Math.max(div - 1, 0);
        return div * (1 + 7) * 7 / 2 + m * (m + 1) * 7 / 2 + (r + 1) * r / 2 + div * r;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    const div = Math.floor(n / 7), r = n % 7, m = Math.max(div - 1, 0)
    return div * (1 + 7) * 7 / 2 + m * (m + 1) * 7 / 2 + (r + 1) * r / 2 + div * r
};
```
```Go []
func totalMoney(n int) int {
    div, r, m := n / 7, n % 7, 0
    if div > 0 {
        m = div - 1
    }
    return div * (1 + 7) * 7 / 2 + m * (m + 1) * 7 / 2 + (r + 1) * r / 2 + div * r
}
```
```C []
int totalMoney(int n){
    int div = n / 7, r = n % 7, m = 0;
    if(div > 0) {
        m = div - 1;
    }
    return div * (1 + 7) * 7 / 2 + m * (m + 1) * 7 / 2 + (r + 1) * r / 2 + div * r;
}
```

稍微整理一下数学公式简化为：
```Python3 []
class Solution:
    def totalMoney(self, n: int) -> int:
        return (div:=n//7) * (div + 7) * 7 // 2 + (1 + (r:=n%7)) * r // 2 + div * r
```
```Java []
class Solution {
    public int totalMoney(int n) {
        int div = n / 7, r = n % 7;
        return div * (div + 7) * 7 / 2 + (r + 1) * r / 2 + div * r;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    const div = Math.floor(n / 7), r = n % 7
    return div * (div + 7) * 7 / 2 + (r + 1) * r / 2 + div * r
};
```
```Go []
func totalMoney(n int) int {
    div, r := n / 7, n % 7
    return div * (div + 7) * 7 / 2 + (r + 1) * r / 2 + div * r
}
```
```C []
int totalMoney(int n){
    int div = n / 7, r = n % 7;
    return div * (div + 7) * 7 / 2 + (r + 1) * r / 2 + div * r;
}
```

### 复杂度
时间复杂度 $o(1)$
空间复杂度 $o(1)$
