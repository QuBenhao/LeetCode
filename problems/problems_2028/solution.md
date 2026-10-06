# [Python/Java/JavaScript/Go] Mathematics

> Author: Benhao
> Date: 2022-03-27
> Upvotes: 11
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
From the average $mean$, the total sum is $sum = mean * (m + n)$.
The input gives the sum of the first $m$ values, so the required sum of the remaining $n$ values is $sum - \sum_{i=1}^mrolls_i$.
Each value must be an integer from 1 to 6, so these $n$ values can produce only sums from $n$ to $6 * n$.

Set every value to the floor of the average (giving a sum of $\lfloor \frac{s}{n} \rfloor * n$), then add one to the first s%n values (adding s%n to the sum).

### Code

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
