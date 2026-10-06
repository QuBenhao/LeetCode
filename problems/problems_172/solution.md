# [Python/Java/JavaScript/Go] Math: count factors of 5

> Author: Benhao
> Date: 2022-03-24
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
A trailing zero is produced by multiplying a positive integer by 10. In other words, each pair of factors 2 and 5 adds a trailing zero to the result.
In a factorial, factors of 2 are far more numerous than factors of 5. Therefore, the number of factors of 5 determines the number of trailing zeros.


Multiples of 5 contribute one factor of 5, such as 5, 10, 15, and 20.
Multiples of $5^2$ contribute two factors of 5, such as 25, 50, 75, and 100.
Multiples of $5^3$ contribute three factors of 5, such as 125, 250, 375, and 500.
...
And so on.


A multiple of $5^i$ has already been counted $i-1$ times when counting multiples of $5$ through $5^{i-1}$. Therefore, count how many multiples of $5^i$ occur and add that count to the answer once more,
namely $\lfloor \frac{n}{5^i} \rfloor$.

The answer is their sum:
$\sum_{i=1}^5 \lfloor \frac{n}{5^i} \rfloor$

[The upper bound here is 5 because the input limit is 10000, and 3125 is the largest power of 5 within that range.]

### Code

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
