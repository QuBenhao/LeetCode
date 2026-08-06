# [Python/Java/TypeScript/Go] 动态规划 及优化

> slug: pythonjavatypescriptgo-by-himymben-gzvy
> date: 2022-06-10
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Flip String to Monotone Increasing (flip-string-to-monotone-increasing)
> url: https://leetcode.cn/problems/flip-string-to-monotone-increasing/solutions/8kn1Rf/pythonjavatypescriptgo-by-himymben-gzvy/

---
### 解题思路
本题其实是枚举一个位置，这个位置左边全变0，右边全变1。
那么我们需要知道这个点左边1的个数，右边0的个数。
预处理这个计数，枚举返回最小值即可。


优化：
注意到右边0的个数其实可以由全部1的个数和左边1的个数和长度计算到，
在最后枚举i的式子中,
r_zeros[i] = (n - i) - (one - l_ones[i])
于是求最小值变为min(l_ones[i] + n - i - one + l_ones[i] for i in range(n)),
我们将n和one常量移到外面，就得到了优化后的动态规划。

时间复杂度$O(n)$
空间复杂度$O(1)$

### 代码

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

优化
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