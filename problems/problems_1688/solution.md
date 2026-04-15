# [Python/Java/JavaScript/Go/C] 基于本题的几种思考方式

> Author: Benhao
> Date: 2022-01-24
> Upvotes: 20
> Tags: C, Go, Java, JavaScript, Python, Python3

---

### 解题思路
1. 递归（数学归纳法）
> 当我们有一支队伍时，不需要比较，
> 即$n = 1$时，$f(1) = 0$
> 当我们有超过一支队伍时，总是可以先比较两队，比较后人数变为n-1,于是有
> $n >= 2$时，$f(n) = 1 + f(n - 1)$
> 这里就可以写出递推的解法了，也可以用数学归纳法求出f(n)的表达式
> $f(n) + f(n-1) + \ldots + f(1) = 1 + f(n-1) + 1 + f(n-2) + \ldots + 1 + f(1) + 0$
> 消元得到$f(n) = n - 1$

2. 二进制
> 本题采取的策略总是除二，和二进制里右移一位相通，那么是否可以用二进制的思想考虑本题呢？
> 由于二的幂次不涉及奇数的轮空问题，所以考虑将原二进制拆成多个二的幂次，
> (注：以下数字均为二进制)
> 举个例子, 10110 变为 10000 + 100 + 10，
> 二的幂次的比赛场数很好计算，【一直右移直到变为1】，也就是10000 比 1111 场, 100 比 11 场， 10 比 1 场
> 那么总场数为 1111 + 11 + 1 + 剩余人数（n的二进制1的个数）需要的比赛场数
> 把多的1优先给原来最左的二进制位，1111就会变为10000

### 代码

```Python3 []
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n - 1
```
```Java []
class Solution {
    public int numberOfMatches(int n) {
        return --n;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var numberOfMatches = function(n) {
    return --n
};
```
```Go []
func numberOfMatches(n int) int {
    return n - 1
}
```
```C []
int numberOfMatches(int n){
    return n - 1;
}
```

题太简单？不如去三叶姐姐那里把[wiki](https://github.com/SharingSource/LogicStack-LeetCode/wiki)刷光