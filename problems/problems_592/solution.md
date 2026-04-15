# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-07-26
> Upvotes: 20
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
首先要写一个从字符串中读取每个分子、分母的功能，
我们不需要计算小数，只需要通分计算最终分子、分母即可。

记住以下两点即可: 
1. 两个不同的分母通分的结果为他们的最小公倍数
2. 一个非最简分数的化简方式为分子分母除去他们的最大公约数

### 代码

```Python3 []
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 可以不单写成函数，放在同一个循环里更简洁
        def read_number(i: int):
            sign, numerator, denominator = -1 if expression[i] == '-' else 1, 0, 0
            if expression[i] in "+-":
                i += 1
            while i < len(expression) and expression[i] != '/':
                numerator = 10 * numerator + int(expression[i])
                i += 1
            i += 1
            while i < len(expression) and expression[i] not in "+-":
                denominator = 10 * denominator + int(expression[i])
                i += 1
            return sign * numerator, denominator if denominator else 1, i
        
        idx = numer = 0
        denom = 1
        while idx < len(expression):
            num, den, idx = read_number(idx)
            lm = lcm(denom, den)
            numer, denom = numer * lm // denom + num * lm // den, lm
        g = gcd(abs(numer), denom)
        return f"{numer // g}/{denom // g}"
```
```Java []
class Solution {
    public String fractionAddition(String expression) {
        long numerator = 0, denominator = 1;
        for (int idx = 0, n = expression.length(); idx < n;) {
            long sign = expression.charAt(idx) == '-' ? -1 : 1, num = 0, den = 0;
            if (expression.charAt(idx) == '-' || expression.charAt(idx) == '+') {
                idx++;
            }
            while (idx < n && expression.charAt(idx) != '/') {
                num = 10 * num + Long.parseLong(expression.substring(idx, idx + 1));
                idx++;
            }
            idx++;
            while (idx < n && expression.charAt(idx) != '-' && expression.charAt(idx) != '+') {
                den = 10 * den + Long.parseLong(expression.substring(idx, idx + 1));
                idx++;
            }
            if (den == 0) {
                den++;
            }
            long lm = lcm(denominator, den);
            numerator = numerator * lm / denominator + num * sign * lm / den;
            denominator = lm;
        }
        long g = gcd(denominator, Math.abs(numerator));
        return String.format("%d/%d", numerator / g, denominator / g);
    }

    public long gcd(long a, long b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public long lcm(long a, long b) {
        return a * b / gcd(a, b);
    }
}
```
```TypeScript []
const neg = '-'.charCodeAt(0), pos = '+'.charCodeAt(0), div = '/'.charCodeAt(0), zero = '0'.charCodeAt(0)
function fractionAddition(expression: string): string {
    const gcd = (a: number, b: number): number => {
        return b == 0 ? a : gcd(b, a % b)
    }, lcm = (a: number, b: number): number => {
        return Math.floor(a * b / gcd(a, b))
    }, n = expression.length
    let numerator = 0, denominator = 1
    for (let idx = 0; idx < n; ) {
        const sign = expression.charCodeAt(idx) === neg ? -1 : 1
        if (expression.charCodeAt(idx) === neg || expression.charCodeAt(idx) === pos) {
            idx++
        }
        let num = 0, den = 0
        while (idx < n && expression.charCodeAt(idx) !== div) {
            num = num * 10 + expression.charCodeAt(idx++) - zero
        }
        idx++
        while (idx < n && expression.charCodeAt(idx) != neg && expression.charCodeAt(idx) != pos) {
            den = den * 10 + expression.charCodeAt(idx++) - zero
        }
        if (den == 0) {
            den++
        }
        const lm = lcm(denominator, den)
        numerator = Math.floor(numerator * lm / denominator) + Math.floor(sign * num * lm / den)
        denominator = lm
    }
    const g = gcd(Math.abs(numerator), denominator)
    return Math.floor(numerator / g) + "/" + Math.floor(denominator / g)
};
```
```Go []
func fractionAddition(expression string) string {
    numerator, denominator := 0, 1
    for idx, n := 0, len(expression); idx < n; {
        sign, num, den := 1, 0, 0
        if expression[idx] == '-' || expression[idx] == '+' {
            if expression[idx] == '-' {
                sign = -1
            }
            idx++
        }
        for idx < n && expression[idx] != '/' {
            num = 10 * num + int(expression[idx] - '0')
            idx++
        }
        idx++
        for idx < n && expression[idx] != '-' && expression[idx] != '+' {
            den = 10 * den + int(expression[idx] - '0')
            idx++
        }
        if den == 0 {
            den++
        }
        lm := lcm(den, denominator)
        numerator = numerator * lm / denominator + sign * num * lm / den
        denominator = lm
    }
    g := gcd(abs(numerator), denominator)
    return fmt.Sprintf("%d/%d", numerator / g, denominator / g)
}

func gcd(a, b int) int {
    if b == 0 {
        return a
    }
    return gcd(b, a % b)
}

func lcm(a, b int) int {
    return a * b / gcd(a, b)
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
```