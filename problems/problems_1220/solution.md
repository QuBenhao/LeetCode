# [Python/Java/JavaScript/Go] 困难题简单做 动态规划->矩阵快速幂模板

> slug: pythonjavajavascriptgo-kun-nan-ti-jian-d-urbm
> date: 2022-01-16
> tags: Go, Java, JavaScript, Python, Python3
> question: Count Vowels Permutation (count-vowels-permutation)
> url: https://leetcode.cn/problems/count-vowels-permutation/solutions/yXEPF1/pythonjavajavascriptgo-kun-nan-ti-jian-d-urbm/

---
### 解题思路
本题的题目描述本身就是动态规划，可以很容易写出递推公式，使用滚动更新的方式节省空间。

动态规划的时间复杂度为$o(n)$，递推写作矩阵乘法的话，会变成相同矩阵的幂次，可以使用矩阵快速幂，时间复杂度$o(\log_2n)$

矩阵快速幂乘法在Js中会出现精度问题，需要手写加法实现的快速乘法。

### 代码
动态规划
```Python3 []
MOD = 10**9 + 7
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e, (a + i) % MOD, (a + e + o + u) % MOD, (i + u) % MOD, a
        return sum([a, e, i, o, u]) % MOD
```
```Java []
class Solution {
    private static final long MOD = (long)1e9 + 7;
    public int countVowelPermutation(int n) {
        long a, e, i, o, u;
        a = e = i = o = u = 1;
        while(--n>0){
            long an, en, in, on, un;
            an = e;
            en = (a + i) % MOD;
            in = ((((a + e) % MOD + o) % MOD) + u) % MOD;
            on = (i + u) % MOD;
            un = a;
            a = an;
            e = en;
            i = in;
            o = on;
            u = un;
        }
        return (int)((((((a + e) % MOD + i) % MOD + o) % MOD) + u) % MOD);
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
const MOD = 1000000007;
var countVowelPermutation = function(n) {
    let a, e, i, o, u;
    a = e = i = o = u = 1;
    while(--n>0){
        var an, en, inxt, on, un;
        an = e;
        en = (a + i) % MOD;
        inxt = ((((a + e) % MOD + o) % MOD) + u) % MOD;
        on = (i + u) % MOD;
        un = a;
        a = an;
        e = en;
        i = inxt;
        o = on;
        u = un;
    }
    return (((((a + e) % MOD + i) % MOD + o) % MOD) + u) % MOD;
};
```
```Go []
const MOD int = 1e9 + 7
func countVowelPermutation(n int) int {
    a, e, i, o, u := 1, 1, 1, 1, 1
    for n := n - 1; n > 0; n-- {
        a, e, i, o, u = e, (a + i) % MOD, (((a + e) % MOD + o) % MOD + u) % MOD, (i + u) % MOD, a
    }
    return ((((a + e) % MOD + i) % MOD + o) % MOD + u) % MOD
}
```
矩阵快速幂
```Python3 []
import numpy as np
MOD = 10 ** 9 + 7
dtype = np.dtype('uint64')
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        A, mul = np.ones(5, dtype=dtype), np.array([[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]],dtype=dtype)
        n -= 1
        while n:
            if n & 1:
                A = A @ mul % MOD
            mul = mul @ mul % MOD
            n >>= 1
        return int(A.sum()) % MOD
```
```Java []
class Solution {
    private static final long MOD = (long)1e9 + 7;
    public int countVowelPermutation(int n) {
        long[][] A = new long[][]{{1,1,1,1,1}}, mul = new long[][]{{0, 1, 1, 0, 1}, {1, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 0, 1, 0, 0}, {0, 0, 1, 1, 0}};
        --n;
        while(n > 0){
            if((n & 1) != 0)
                A = multiply(A, mul);
            mul = multiply(mul, mul);
            n >>= 1;
        }
        long ans = 0L;
        for(int i=0;i < A.length;i++)
            for(int j=0;j < A[0].length;j++)
                ans = (ans + A[i][j]) % MOD;
        return (int)ans;
    }

    private long[][] multiply(long[][] A, long[][] B){
        long[][] res = new long[A.length][B[0].length];
        for(int i=0;i<res.length;i++)
            for(int j=0;j<res[0].length;j++)
                for(int k=0;k<A[0].length;k++)
                    res[i][j] = (res[i][j] + A[i][k] * B[k][j] % MOD) % MOD;
        return res;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {number}
 */
const MOD = 1000000007;
var countVowelPermutation = function(n) {
    fastPlus = (a, b, m) => {
        let s = a + b;
        if (s >= a && s >= b) return s % m;
        if (a > m) return plus(a % m, b, m);
        if (b > m) return plus(a, b % m, m);
        return a - m + b;
    }
    
    fastMul = (a, b, m) => {
        let ret = 0;
        a %= m, b %= m;
        while (b) {
            if(b & 1) ret = fastPlus(ret, a, m);
            b = Math.floor(b / 2), a = fastPlus(a, a, m);
        }
        return ret;
    }

    multiply = function(X, Y){
        const res = new Array(X.length)
        for(let i=0;i < X.length;i++){
            res[i] = new Array(Y[0].length)
            res[i].fill(0)
        }
        for(let i=0;i < res.length;i++)
            for(let j=0;j < res[0].length;j++)
                for(let k=0;k < Y.length;k++)
                    res[i][j] = (res[i][j] + fastMul(X[i][k], Y[k][j], MOD)) % MOD
        return res
    }

    let A = [[1, 1, 1, 1, 1]], mul = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0]]
    --n
    while(n > 0){
        if((n & 1) != 0)
            A = multiply(A, mul)
        mul = multiply(mul, mul)
        n >>= 1
    }
    let ans = 0
    for(let i=0;i < A.length;i++)
        for(let j=0;j < A[0].length;j++)
            ans = (ans + A[i][j]) % MOD
    return ans
};
```
```Go []
const MOD int = 1e9 + 7

func countVowelPermutation(n int) (ans int) {
    multiply := func(X, Y [][]int) [][]int{
        res := make([][]int, len(X))
        for i := 0;i < len(res);i++{res[i] = make([]int, len(Y[0]))}
        for i := 0;i < len(res);i++{
            for j := 0;j < len(res[0]);j++{
                for k := 0;k < len(Y);k++{
                    res[i][j] = (res[i][j] + X[i][k] * Y[k][j] % MOD) % MOD
                }
            }
        }
        return res
    }

    A, mul := [][]int{{1, 1, 1, 1, 1}}, [][]int{{0, 1, 1, 0, 1}, {1, 0, 1, 0, 0}, {0, 1, 0, 1, 0}, {0, 0, 1, 0, 0}, {0, 0, 1, 1, 0}}
    n--
    for n > 0 {
        if(n & 1 != 0){
            tmp := multiply(A, mul)
            A = tmp
        }
        tmpB := multiply(mul, mul)
        mul = tmpB
        n >>= 1
    }
    for _, row := range A {
        for _, cell := range row{
            ans = (ans + cell) % MOD
        }
    }
    return
}
```