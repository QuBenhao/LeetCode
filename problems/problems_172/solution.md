# [Python/Java/JavaScript/Go] 数学 - 统计5的因子个数

> Author: Benhao
> Date: 2022-03-24
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
末尾0其实是任意正整数乘以10产生的，也就是说因子中每出现一个2和一个5，结果就会多一个末尾0。
显然连续数字的阶乘里，2的因子个数是远远多于5的因子个数的。那么主要影响末尾0的个数其实是5的因子个数。


5的倍数会产生一个5的因子，比如5、10、15、20
$5^2$的倍数会产生两个5的因子，比如25、50、75、100
$5^3$的倍数会产生三个5的因子，比如125、250、375、500
...
以此类推


对于$5^i$的因子的倍数，在统计$5$到$5^{i-1}$个的倍数时，已经被计算了$i-1$次了，那么只需要单独统计$5^i$倍数出现了多少次再累加一次到答案即可,
也即$\lfloor \frac{n}{5^i} \rfloor$。

答案即为他们的和：
$\sum_{i=1}^5 \lfloor \frac{n}{5^i} \rfloor$

【这里上届为5是因为输入范围为10000，3125为这个范围内最大的5的次方】

### 代码

```Python3 []
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return sum(n // 5 ** i for i in range(1, 6))
```
```Java []
class Solution {
    private static final int[] FIVES = new int[5];
    static {
        int cur = 5, idx = 0;
        while(cur <= 10000) {
            FIVES[idx++] = cur;
            cur *= 5;
        }
    }

    public int trailingZeroes(int n) {
        int ans = 0;
        for(int five: FIVES)
            ans += n / five;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
var trailingZeroes = function(n) {
    return n > 0 ? Math.floor(n / 5) + trailingZeroes(Math.floor(n / 5)) : 0
};
```
```Go []
func trailingZeroes(n int) (ans int) {
    for n > 0 {
        n /= 5
        ans += n
    }
    return
}
```