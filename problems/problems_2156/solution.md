# [Python/Go] 倒序滑动窗口 or 正向滑窗乘法逆元(扩展欧几里德)

> Author: Benhao
> Date: 2022-01-30
> Upvotes: 26
> Tags: Go, Python, Python3

---

### 解题思路
容易想到一个长度为k的滑动窗口。

给出的哈希计算函数是一个等比求和数列，两者可以通过减去首元素，除以power再加上新元素的power的k-1次方计算。
但是这个的问题在于除法不满足取余的恒等性。(本题的power和modulo也不一定满足互质)
因此需要倒序，减去当前的值，乘以power再加上新元素的值。（乘法满足取余恒等）

关于除法取模，感兴趣的了解一下[逆元](https://blog.csdn.net/LeBron_Yang/article/details/82948732)

### 代码

```Python3
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        t = pow(power, k - 1, modulo)
        val = ans = 0
        for i in range(k):
            val = (val + (ord(s[len(s) - 1 -i]) - ord('a') + 1) * pow(power, k - 1 - i, modulo) % modulo) % modulo
        if val == hashValue:
            ans = len(s) - k
        for i in range(len(s) - 1, k - 1, -1):
            val = (val - (ord(s[i]) - ord('a') + 1) * t % modulo) % modulo
            val = val * power  % modulo
            val = (val + ord(s[i - k]) - ord('a') + 1) % modulo 
            if val == hashValue:
                ans = i - k
        return s[ans:ans+k]
```

利用python3.8新特性，`pow(p, -1, mod)`直接求解乘法逆元
```Python3
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        def val(c):
            return ord(c) - ord('a') + 1
        
        if gcd(power, modulo) > 1:
            t = pow(power, k - 1, modulo)
            val = ans = 0
            for i in range(k):
                val = (val + (ord(s[len(s) - 1 -i]) - ord('a') + 1) * pow(power, k - 1 - i, modulo) % modulo) % modulo
            if val == hashValue:
                ans = len(s) - k
            for i in range(len(s) - 1, k - 1, -1):
                val = (val - (ord(s[i]) - ord('a') + 1) * t % modulo) % modulo
                val = val * power  % modulo
                val = (val + ord(s[i - k]) - ord('a') + 1) % modulo 
                if val == hashValue:
                    ans = i - k
            return s[ans:ans+k]

        v = 0
        for i in range(k):
            v = (v + val(s[i]) * pow(power, i, modulo)) % modulo
        if v == hashValue:
            return s[:k]
        for i in range(k, len(s)):
            v = (v - val(s[i - k])) % modulo
            v = v * pow(power, -1, modulo) % modulo
            v = (v + val(s[i]) * pow(power, k - 1, modulo)) % modulo
            if v == hashValue:
                return s[i - k + 1:i + 1]
        return ""
```

【进阶】Go语言扩展欧几里德
```Go
func subStrHash(s string, power int, modulo int, k int, hashValue int) string {
    val := func(b byte) int {
        return int(b - 'a') + 1
    }

    v, p, n := 0, 1, len(s)
    if gcd(power, modulo) > 1 {
        // 倒序
        ans := -1
        for i := n - k; i < n; i++ {
            v = (v + val(s[i]) * p % modulo) % modulo
            if i < n - 1 {
                p = p * power % modulo
            }
        }
        if v == hashValue {
            ans = n - k
        }
        for i := n - k - 1; i >= 0; i-- {
            v = ((v - val(s[i + k]) * p % modulo + modulo) % modulo * power % modulo + val(s[i])) % modulo
            if v == hashValue {
                ans = i
            }
        }
        return s[ans:ans+k]
    } else {
        // 因为modulo不一定是质数，费马小定理不一定成立。需使用扩展欧几里德
        np, _, _ := Exgcd(power, modulo)
        np = (np + modulo) % modulo
        for i := 0; i < k; i++ {
            v = (v + val(s[i]) * p % modulo) % modulo
            if i < k - 1 {
                p = p * power % modulo
            }
        }
        if v == hashValue {
            return s[:k]
        }
        for i := k; i < n; i++ {
            v = (v - val(s[i - k]) + modulo) % modulo * np % modulo
            v = (v + val(s[i]) * p % modulo) % modulo
            if v == hashValue {
                return s[i - k + 1: i + 1]
            }
        }
    }
    return ""
}

// 最大公约数
func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

// 快速幂
func pow(p, n, mod int) int {
	ans := int64(1)
	pN, modN := int64(p), int64(mod)
	for n > 0 {
		if n & 1 == 1 {
			ans = ans * pN % modN
		}
		pN = pN * pN % modN
		n >>= 1
	}
	return int(ans)
}

// 扩展欧几里德 a * x + b * y = 1
// 求x, y，使得ax + by = gcd(a, b)
func Exgcd(a, b int) (o, p, q int) {
    if b == 0 {
        return 1, 0, a
    }
    x, y, d := Exgcd(b,a%b)
    return y, x - a / b * y, d
}
```