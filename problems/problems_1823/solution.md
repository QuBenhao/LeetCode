# [Python/Java/JavaScript/Go] 约瑟夫环

> Author: Benhao
> Date: 2022-05-03
> Upvotes: 73
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
很经典的题。

我们第一轮会删掉第$k$个人，问题就变为对$n-1$个人进行这个游戏。
假设我们知道$f(n-1,k)$最终剩下的人的编号,
由于我们删了第$k$个人，$n-1$个人的游戏是从原来第$k+1$个人开始的，
也就是说原来的编号和新的编号有一个偏差$k$。
以坐标从$0$到$n-1$来看的话(去掉1的偏差减少计算量,最终加一次1即可)，有公式:
$f(n,k) = (f(n - 1, k) + k) \% n$

当只剩一个人时，他必然活下来，
即$f(1,k) = 0$,
我们从$f(1,k)$推出$f(2,k)$一直到$f(n,k)$即可。

### 代码

```Python3 []
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1
```
```Java []
class Solution {
    public int findTheWinner(int n, int k) {
        int ans = 0;
        for(int i = 2; i <= n; i++)
            ans = (ans + k) % i;
        return ans + 1;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var findTheWinner = function(n, k) {
    let ans = 0
    for(let i = 2; i <= n; i++)
        ans = (ans + k) % i
    return ans + 1
};
```
```Go []
func findTheWinner(n int, k int) (ans int) {
    for i := 2; i <= n; i++ {
        ans = (ans + k) % i
    }
    ans++
    return
}
```