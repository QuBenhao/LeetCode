# [Python/Java/JavaScript/Go] 数学

> Author: Benhao
> Date: 2022-03-27
> Upvotes: 11
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
根据平均数$mean$，我们知道全部的和为$sum = mean * (m + n)$。
而根据输入可以求得前$m$个数的和，于是需要的$n$个数的和为$sum - \sum_{i=1}^mrolls_i$。
由于每个数只能是1到6之间的整数，最终这$n$个数的和只能构造出$n$到$6 * n$之间的数。

构造方法为每个数都至少为和的平均数 (这样和为$\lfloor \frac{s}{n} \rfloor * n$)，前面和的余数个数加额外的一(这样加的和为s%n)即可。

### 代码

```python3 []
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        return [s // n + 1] * (s % n) + [s // n] * (n - s % n) if n <= (s := mean * (len(rolls) + n) - sum(rolls)) <= 6 * n else []
```
```Java []
class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int s = mean * (rolls.length + n);
        for(int roll: rolls) {
            s -= roll;
        }
        if(s < n || s > 6 * n)
            return new int[]{};
        int[] ans = new int[n];
        int d = s / n;
        for(int i = 0; i < s % n; i++)
            ans[i] = d + 1;
        for(int i = s % n; i < n; i++)
            ans[i] = d;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    let s = mean * (rolls.length + n)
    for(const roll of rolls)
        s -= roll
    if(s < n || s > 6 * n)
        return new Array()
    const ans = new Array(n).fill(Math.floor(s / n))
    for(let i = 0; i < s % n; i++)
        ans[i]++
    return ans
};
```
```Go []
func missingRolls(rolls []int, mean int, n int) []int {
    s := mean * (len(rolls) + n)
    for _, roll := range rolls {
        s -= roll
    }
    if s < n || s > 6 * n {
        return []int{}
    }
    ans, d := make([]int, n), s / n
    for i := 0; i < s % n; i++ {
        ans[i] = d + 1
    }
    for i := s % n; i < n; i++ {
        ans[i] = d
    }
    return ans
}
```