# [Python/Java/TypeScript/Go] 模拟

> Author: Benhao
> Date: 2022-08-09
> Upvotes: 28
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
将式子解析为"k * x = val"，再分析答案即可。

### 代码

```Python3 []
class Solution:
    def solveEquation(self, equation: str) -> str:
        # sign: 当前正负, cur: 当前数字, num: 等式的数字项大小, k: 等式x的系数, left: 是否在等号左, has_val: 当前有没有出现任何数字
        sign, cur, num, k, left, has_val = 1, 0, 0, 0, True, False
        for c in equation + "=":
            if c in "-+=x":
                if c == 'x':
                    if not has_val and not cur:
                        cur = 1
                    k += sign * cur if left else -sign * cur
                else:
                    num += sign * cur if not left else -sign * cur
                cur, has_val = 0, False
            match c:
                case "-":
                    sign = -1
                case "+":
                    sign = 1
                case "=":
                    sign, left = 1, False
                case "x":
                    pass
                case _:
                    cur, has_val = cur * 10 + int(c), True
        if not k:
            return "No solution" if num else "Infinite solutions"
        return f"x={num//k}" if not (num % k) else "No solution"
```
```Java []
class Solution {
    private static final String CHARS = "-+x=";
    public String solveEquation(String equation) {
        equation += "=";
        int sign = 1, cur = 0, num = 0, k = 0;
        boolean hasVal = false, left = true;
        for (int i = 0; i < equation.length(); i++) {
            char c = equation.charAt(i);
            if (CHARS.contains(String.valueOf(c))) {
                if (c == 'x') {
                    if (!hasVal && cur == 0) {
                        cur = 1;
                    }
                    k += left ? sign * cur : -sign * cur;
                } else {
                    num -= left ? sign * cur: -sign * cur;
                }
                cur = 0;
                hasVal = false;
            }
            switch (c) {
                case '-':
                    sign = -1;
                    break;
                case '+':
                    sign = 1;
                    break;
                case '=':
                    sign = 1;
                    left = false;
                    break;
                case 'x':
                    break;
                default:
                    cur = cur * 10 + (c - '0');
                    hasVal = true;
            }
        }
        if (k == 0) {
            return num != 0 ? "No solution" : "Infinite solutions";
        }
        return num % k == 0 ? String.format("x=%d", num/k) : "No solution";
    }
}
```
```TypeScript []
const CHARS: string = "-+=x";
function solveEquation(equation: string): string {
    equation += "="
    let sign = 1, cur = 0, num = 0, k = 0, left = true, hasVal = false
    for (let i = 0; i < equation.length; i++) {
        const c: string = equation.charAt(i)
        if (CHARS.includes(c)) {
            if (c == "x") {
                if (!hasVal && cur == 0) {
                    cur = 1
                }
                k += left ? sign * cur : -sign * cur
            } else {
                num -= left ? sign * cur: -sign * cur
            }
            cur = 0
            hasVal = false
        }
        switch (c) {
            case '-':
                sign = -1
                break
            case '+':
                sign = 1
                break
            case '=':
                sign = 1
                left = false
                break
            case 'x':
                break
            default:
                cur = cur * 10 + equation.charCodeAt(i) - '0'.charCodeAt(0)
                hasVal = true
            }
    }
    if (k == 0) {
        return num != 0 ? "No solution" : "Infinite solutions"
    }
    return num % k == 0 ? "x=" + Math.floor(num/k) : "No solution"
};
```
```Go []
func solveEquation(equation string) string {
    equation += "="
    sign, cur, num, k, left, has_val := 1, 0, 0, 0, true, false
    for i := 0; i < len(equation); i++ {
        if equation[i] == '-' {
            if !left {
                num += sign * cur
            } else {
                num -= sign * cur
            }
            cur, has_val, sign = 0, false, -1
        } else if equation[i] == '+' {
            if !left {
                num += sign * cur
            } else {
                num -= sign * cur
            }
            cur, has_val, sign = 0, false, 1
        } else if equation[i] == '=' {
            if !left {
                num += sign * cur
            } else {
                num -= sign * cur
            }
            cur, has_val, sign, left = 0, false, 1, false
        } else if equation[i] == 'x' {
            if !has_val && cur == 0 {
                cur = 1
            }
            if left {
                k += sign * cur
            } else {
                k -= sign * cur
            }
            cur, has_val = 0, false
        } else {
            has_val = true
            cur = cur * 10 + int(equation[i] - '0')
        }
    }
    if k == 0 {
        if num != 0 {
            return "No solution"
        }
        return "Infinite solutions"
    }
    if num % k == 0 {
        return "x=" + strconv.Itoa(num/k)
    }
    return "No solution"
}
```