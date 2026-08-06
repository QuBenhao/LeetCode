# [Python/Java/JavaScript/Go] 贪心选取最接近k的斐波那契数的证明

> slug: pythonjavajavascriptgo-tan-xin-xuan-qu-z-7b0g
> date: 2022-02-03
> tags: Go, Java, JavaScript, Python, Python3
> question: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K (find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k)
> url: https://leetcode.cn/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/solutions/wtk2g7/pythonjavajavascriptgo-tan-xin-xuan-qu-z-7b0g/

---
### 解题思路
我们最终选取的数列中的数必然没有相邻的，因为相邻的话我们可以直接取下一个斐波那契数（它们的和），毕竟取一个比取两个肯定取了更少的数。
根据这一条件证明我们必须选最接近k的斐波那契数。

反证法：
假设最接近$k$的斐波那契数为$F_m$ (即$F_m <= k$)，且我们最终答案不能取$F_m$。
那么我们最大的取法为$F_{m-1} + F_{m-3} + \ldots + F_1$ (m为偶数时) 以及 $F_{m-1} + F_{m-3} + \ldots + F_2$ (m为奇数时)
$F_{m} = F_{m-1} + F_{m-2} = F_{m-1} + F_{m-3} + F_{m-4} = \ldots = F_{m-1} + F_{m-3} + \ldots + F_2 + F_1 > F_{m-1} + F_{m-3} + \ldots + F_1$
不论m是奇数还是偶数，我们将$F_m$展开都会发现，$k >= F_{m} = F_{m-1} + F_{m-3} + \ldots + F_1 (m为偶数) 或 $k >= F_{m} = F_{m-1} + F_{m-3} + \ldots + F_2 + 1 > F_{m-1} + F_{m-3} + \ldots + F_2$ (m为奇数)
也就是说，不取$F_m$且不取相邻的斐波那契数我们最大取到$F_{m}$，如果$k$本身等于$F_{m}$，那么取一个数必然更优，否则必不可能取到$k$

故，最接近k的斐波那契数必须被选。取完后后面依然是一个递归求解。

> 如果不好理解的话，用大白话说就是 1，1，2，3，5，8，13 这个数列中，你会发现 13比 8 + 3 + 1 大1。8等于5 + 2 + 1。

### 代码

```python3 []
class Solution:
    @lru_cache(None)
    def findMinFibonacciNumbers(self, k: int) -> int:
        if not k:
            return 0
        f, f1 = 1, 1
        while f1 <= k:
            f, f1 = f1, f + f1
        return 1 + self.findMinFibonacciNumbers(k - f)
```
```Java []
class Solution {
    public int findMinFibonacciNumbers(int k) {
        if(k == 0)
            return 0;
        int f0 = 1, f1 = 1;
        while(f1 <= k){
            int tmp = f0;
            f0 = f1;
            f1 += tmp;
        }
        return 1 + findMinFibonacciNumbers(k - f0);
    }
}
```
```JavaScript []
/**
 * @param {number} k
 * @return {number}
 */
var findMinFibonacciNumbers = function(k) {
    if(k == 0)
        return 0
    let f = 1, f1 = 1
    while(f1 <= k){
        const tmp = f
        f = f1
        f1 += tmp
    }
    return 1 + findMinFibonacciNumbers(k - f)
};
```
```Go []
func findMinFibonacciNumbers(k int) int {
    if k == 0 {
        return 0
    }
    f, f1 := 1, 1
    for f1 <= k {
        f, f1 = f1, f + f1
    }
    return 1 + findMinFibonacciNumbers(k - f)
}
```