# [Python/Java/JavaScript/Go] Brute-force simulation -> prime sieve

> slug: pythonjavajavascriptgo-su-shu-shai-by-hi-5i6z
> date: 2022-02-09
> tags: Go, Java, JavaScript, Python, Python3
> question: Simplified Fractions (simplified-fractions)
> url: https://leetcode.cn/problems/simplified-fractions/solutions/Dc1mTb/pythonjavajavascriptgo-su-shu-shai-by-hi-5i6z/

---
### Approach
Check whether each numerator has greatest common divisor 1 with the current denominator.

Precompute all primes up to n. Factor each candidate denominator, then use its prime factors to generate all numerators that are not coprime with it. Add all remaining numerators to the answer.

### Code

```Python3 []
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return ["{}/{}".format(j, i) for i in range(2, n + 1) for j in range(1, i) if gcd(j, i) == 1]
```
```Java []
class Solution {
    public List<String> simplifiedFractions(int n) {
        List<String> ans = new ArrayList<>();
        for(int i = 2; i <= n; i++)
            for(int j = 1; j < i; j++)
                if(gcd(i, j) == 1)
                    ans.add(String.format("%d/%d", j, i));
        return ans;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {string[]}
 */
var simplifiedFractions = function(n) {
    gcd = function(a, b) {
        return b == 0 ? a : gcd(b, a % b)
    }
    ans = new Array()
    for(let i = 2; i <= n; i++) 
        for(let j = 1; j < i; j++)
            if(gcd(i, j) == 1)
                ans.push(j + "/" + i) 
    return ans
};
```
```Go []
func simplifiedFractions(n int) (ans []string) {
    for i := 2 ; i <= n; i++ {
        for j := 1; j < i; j++ {
            if gcd(i, j) == 1 {
                ans = append(ans, fmt.Sprintf("%d/%d", j, i))
            }
        }
    }
    return
}

func gcd(a, b int) int {
    if b == 0 {
        return a
    }
    return gcd(b, a % b)
}
```
```python3
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        isPrime = [True] * (n + 1)
        primes = []
        for i in range(2, n + 1):
            if isPrime[i]:
                for j in range(i * i, n + 1, i):
                    isPrime[j] = False
                primes.append(i)
        ans = []
        # Enumerate denominators
        for i in range(2, n + 1):
            if isPrime[i]:
                ans += ["{}/{}".format(j, i) for j in range(1, i)]
            else:
                idx, ps = 0, set()
                # All prime factors of the denominator
                while idx < len(primes) and primes[idx] < i // 2 + 1:
                    if not i % primes[idx]:
                        ps.add(primes[idx])
                    idx += 1
                s = set()
                # Generate all numerators whose greatest common divisor with the denominator is not 1
                for p in ps:
                    for j in range(p, i, p):
                        s.add(j)
                ans += ["{}/{}".format(j, i) for j in range(1, i) if j not in s]
        return ans
```
