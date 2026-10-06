# [Python/Go] Reverse sliding window, or a forward window with modular inverses (extended Euclidean algorithm)

> Author: Benhao
> Date: 2022-01-30
> Upvotes: 26
> Tags: Go, Python, Python3

---

### Approach
A sliding window of length k is a natural choice.

The hash is a sum weighted by powers of a common ratio. To move the window forward, subtract the first element, divide by power, then add the new element multiplied by power to the k-1.
The difficulty is that ordinary division does not preserve modular equivalence. (Here, power and modulo are not necessarily coprime either.)
Traverse in reverse instead: subtract the outgoing contribution, multiply by power, then add the incoming element. Multiplication preserves modular equivalence.

For modular division, see this explanation of [modular inverses](https://blog.csdn.net/LeBron_Yang/article/details/82948732).

### Code

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

Use the feature added in Python 3.8: `pow(p, -1, mod)` directly computes the modular multiplicative inverse.
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

[Advanced] Extended Euclidean algorithm in Go
```Go
func subStrHash(s string, power int, modulo int, k int, hashValue int) string {
    val := func(b byte) int {
        return int(b - 'a') + 1
    }

    v, p, n := 0, 1, len(s)
    if gcd(power, modulo) > 1 {
        // Reverse order
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
        // modulo is not necessarily prime, so Fermat's little theorem may not apply; use the extended Euclidean algorithm
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

// Greatest common divisor
func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

// Fast exponentiation
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

// Extended Euclidean algorithm: a * x + b * y = 1
// Find x and y such that ax + by = gcd(a, b)
func Exgcd(a, b int) (o, p, q int) {
    if b == 0 {
        return 1, 0, a
    }
    x, y, d := Exgcd(b,a%b)
    return y, x - a / b * y, d
}
```
