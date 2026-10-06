# [Python/Java/JavaScript/Go] Proof of greedily choosing the Fibonacci number closest to k

> slug: pythonjavajavascriptgo-tan-xin-xuan-qu-z-7b0g
> date: 2022-02-03
> tags: Go, Java, JavaScript, Python, Python3
> question: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K (find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k)
> url: https://leetcode.cn/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/solutions/wtk2g7/pythonjavajavascriptgo-tan-xin-xuan-qu-z-7b0g/

---
### Approach
The chosen numbers cannot be adjacent in the Fibonacci sequence: two adjacent numbers can be replaced by the next Fibonacci number, their sum, and one number is fewer than two.
Use this condition to prove that the Fibonacci number closest to k must be chosen.

Proof by contradiction:
Suppose the Fibonacci number closest to $k$ is $F_m$ (with $F_m <= k$), and assume the final answer cannot use $F_m$.
The largest possible choice is then $F_{m-1} + F_{m-3} + \ldots + F_1$ when m is even, or $F_{m-1} + F_{m-3} + \ldots + F_2$ when m is odd.
$F_{m} = F_{m-1} + F_{m-2} = F_{m-1} + F_{m-3} + F_{m-4} = \ldots = F_{m-1} + F_{m-3} + \ldots + F_2 + F_1 > F_{m-1} + F_{m-3} + \ldots + F_1$
Whether m is odd or even, expanding $F_m$ gives $k >= F_{m} = F_{m-1} + F_{m-3} + \ldots + F_1$ (m even), or $k >= F_{m} = F_{m-1} + F_{m-3} + \ldots + F_2 + 1 > F_{m-1} + F_{m-3} + \ldots + F_2$ (m odd).
In other words, without $F_m$ or adjacent Fibonacci numbers, the largest sum is $F_{m}$. If $k$ equals $F_{m}$, using that single number is better; otherwise, reaching $k$ is impossible.

Therefore, the Fibonacci number closest to k must be chosen. The remainder is another instance of the same recursive problem.

> Put simply, in the sequence 1, 1, 2, 3, 5, 8, 13, the value 13 exceeds 8 + 3 + 1 by 1, while 8 equals 5 + 2 + 1.

### Code

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
