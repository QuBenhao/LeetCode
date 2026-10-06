# [Python/Java/TypeScript/Go] Dynamic programming and optimization

> slug: pythonjavatypescriptgo-by-himymben-gzvy
> date: 2022-06-10
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Flip String to Monotone Increasing (flip-string-to-monotone-increasing)
> url: https://leetcode.cn/problems/flip-string-to-monotone-increasing/solutions/8kn1Rf/pythonjavatypescriptgo-by-himymben-gzvy/

---
### Approach
Enumerate a split position: turn everything to its left into 0 and everything to its right into 1.
We need the number of ones on its left and zeros on its right.
Precompute these counts, enumerate the positions, and return the minimum.


Optimization:
The number of zeros on the right can be computed from the total number of ones, the number of ones on the left, and the length.
In the final expression that enumerates i,
r_zeros[i] = (n - i) - (one - l_ones[i])
the minimum becomes min(l_ones[i] + n - i - one + l_ones[i] for i in range(n)),
Move the constants n and one outside to obtain the optimized dynamic program.

Time complexity: $O(n)$
Space complexity: $O(1)$

### Code

```Python3 []
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        l_ones, r_zeros = [0] * n, [0] * n
        one = 0
        for i in range(n):
            l_ones[i] = one
            one += s[i] == '1'
        zero = 0
        for i in range(n - 1, -1, -1):
            zero += s[i] == '0'
            r_zeros[i] = zero
        return min(min(l_ones[i] + r_zeros[i] for i in range(n)), zero, one)
```
```Java []
class Solution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        int[] lOnes = new int[n], rZeros = new int[n];
        int one = 0;
        for (int i = 0; i < n; i++) {
            lOnes[i] = one;
            if (s.charAt(i) == '1') {
                one++;
            }
        }
        for (int i = n - 1, zero = 0; i >= 0; i--) {
            if (s.charAt(i) == '0') {
                zero++;
            }
            rZeros[i] = zero;
        }
        for (int i = 0; i < n; i++) {
            one = Math.min(one, lOnes[i] + rZeros[i]);
        }
        return one;
    }
}
```
```TypeScript []
function minFlipsMonoIncr(s: string): number {
    const n = s.length
    const lOnes = new Array(n).fill(0), rZeros = new Array(n).fill(0)
    let one = 0
    for (let i = 0; i < n; i++) {
        lOnes[i] = one
        if (s.charCodeAt(i) === '1'.charCodeAt(0)) {
            one++
        }
    }
    for (let i = n - 1, zero = 0; i >= 0; i--) {
        if (s.charCodeAt(i) === '0'.charCodeAt(0)) {
            zero++
        }
        rZeros[i] = zero
    }
    for (let i = 0; i < n; i++) {
        one = Math.min(one, lOnes[i] + rZeros[i])
    }
    return one
};
```
```Go []
func minFlipsMonoIncr(s string) (ans int) {
    n := len(s)
    lOnes, rZeros := make([]int, n), make([]int, n)
    for i := 0; i < n; i++ {
        lOnes[i] = ans
        if s[i] == '1' {
            ans++
        }
    }
    for i, zero := n - 1, 0; i >= 0; i-- {
        if s[i] == '0' {
            zero++
        }
        rZeros[i] = zero
    }
    for i := 0; i < n; i++ {
        ans = min(ans, lOnes[i] + rZeros[i])
    }
    return ans
}

func min(vals ...int) int {
    ans := vals[0]
    for _, v := range vals[1:] {
        if v < ans {
            ans = v
        }
    }
    return ans
}
```

Optimization
```Python3 []
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        one, ans = 0, inf
        for i in range(n):
            ans = min(ans, 2 * one - i)
            one += s[i] == '1'
        return min(ans + n - one, one)
```
```Java []
class Solution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length(), one = 0, ans = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            ans = Math.min(ans, one * 2 - i);
            if (s.charAt(i) == '1') {
                one++;
            }
        }
        return Math.min(one, ans + n - one);
    }
}
```
```TypeScript []
function minFlipsMonoIncr(s: string): number {
    const n = s.length
    let one = 0, ans = Number.MAX_SAFE_INTEGER
    for (let i = 0; i < n; i++) {
        ans = Math.min(ans, one * 2 - i)
        if (s.charCodeAt(i) == '1'.charCodeAt(0)) {
            one++
        }
    }
    return Math.min(one, ans + n - one)
};
```
```Go []
func minFlipsMonoIncr(s string) int {
    n := len(s)
    one, ans := 0, 0
    for i := 0; i < n; i++ {
        ans = min(ans, one * 2 - i)
        if s[i] == '1' {
            one++
        }
    }
    return min(one, ans + n - one)
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```
