# [Python/Java/JavaScript/Go] 快速幂 

> slug: pythonjavajavascriptgo-kuai-su-mi-by-him-0hhe
> date: 2021-12-05
> tags: Go, Java, JavaScript, Python, Python3
> question: Super Pow (super-pow)
> url: https://leetcode.cn/problems/super-pow/solutions/JPLCxX/pythonjavajavascriptgo-kuai-su-mi-by-him-0hhe/

---
# 解题思路

归根结底就是
同底数幂运算公式: $p^{a + b} = p^{a} * p^{b}$
和
幂的乘方: $(p^a)^b = p^{a * b}$

[叶总题解](https://leetcode.cn/problems/super-pow/solution/gong-shui-san-xie-di-gui-kuai-su-mi-ying-yx1j/)
[快速幂算法讲解](https://zhuanlan.zhihu.com/p/95902286)

# 代码
```python3
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join(map(str,b))), 1337)
```
```Python3 []
MOD = 1337
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def dfs(i):
            if i == -1:
                return 1
            return quickPow(dfs(i - 1), 10) * quickPow(a, b[i]) % MOD
        
        def quickPow(x, y):
            ans = 1
            x %= MOD
            while y:
                if y & 1:
                    ans = ans * x % MOD
                x = x * x % MOD
                y >>= 1
            return ans
        
        a %= MOD
        return dfs(len(b) - 1)
```
```Java []
class Solution {
    private static final int MOD = 1337;
    public int superPow(int a, int[] b) {
        return dfs(a % MOD, b, b.length - 1);
    }

    private int dfs(int a, int[] b, int idx) {
        if(idx == -1 || a == 1)
            return 1;
        return qPow(dfs(a, b, idx - 1),10) * qPow(a, b[idx]) % MOD;
    }

    private int qPow(int a, int b) {
        int ans = 1;
        a %= MOD;
        while(b > 0){
            if((b & 1) !=0)
                ans = ans * a % MOD;
            a = a * a % MOD;
            b >>= 1;
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} a
 * @param {number[]} b
 * @return {number}
 */
const MOD = 1337
var superPow = function(a, b) {
    dfs = function(idx) {
        if(idx == -1)
            return 1
        return quickPow(dfs(idx-1), 10) * quickPow(a, b[idx]) % MOD
    }

    quickPow = function(x, y){
        let ans = 1
        x %= MOD
        while(y != 0){
            if((y & 1) != 0)
                ans = ans * x % MOD
            x = x * x % MOD
            y >>= 1
        }
        return ans
    }

    a %= MOD
    return dfs(b.length-1)
};
```
```Go []
func superPow(a int, b []int) int {
    var dfs func(a, mod int, b[] int) int
    dfs = func(a, mod int, b[] int) int {
        if len(b) == 0 || a == 1 {
            return 1
        }
        return quickPow(dfs(a, mod, b[:len(b)-1]), 10, mod) * quickPow(a, b[len(b)-1], mod) % mod 
    }

    mod := 1337
    a %= mod
    return dfs(a, mod, b)
}

func quickPow(a, b, mod int) int {
    ans := 1
    a %= mod
    for b != 0 {
        if (b & 1) == 1 {
            ans = ans * a % mod
        }
        a = a * a % mod
        b >>= 1
    }
    return ans
}
```