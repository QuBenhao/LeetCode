# [Python/Java/JavaScript/Go] 字符串模拟

> slug: pythonjavajavascriptgo-zi-fu-chuan-mo-ni-wvl8
> date: 2022-02-24
> tags: Go, Java, JavaScript, Python, Python3
> question: Complex Number Multiplication (complex-number-multiplication)
> url: https://leetcode.cn/problems/complex-number-multiplication/solutions/AjAwnL/pythonjavajavascriptgo-zi-fu-chuan-mo-ni-wvl8/

---
### 解题思路
字符串解析成实部、虚部，然后应用多项式乘多项式展开，得到最终的实部、虚部

ps：
不使用库函数可以做一次小模拟练习

### 代码

```Python3 []
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # (a0 + b0*i) * (a1 + b1*i) = (a0 * a1 - b0 * b1) + (a0 * b1 + a1 * b0) * i
        a0, b0 = map(int, num1[:-1].split("+"))
        a1, b1 = map(int, num2[:-1].split("+"))
        return "{}+{}i".format(a0 * a1 - b0 * b1, a0 * b1 + a1 * b0)
```
```Java []
class Solution {
    public String complexNumberMultiply(String num1, String num2) {
        int[] n1 = convert(num1), n2 = convert(num2);
        return String.format("%d+%di", n1[0] * n2[0] - n1[1] * n2[1], n1[0] * n2[1] + n1[1] * n2[0]);
    }

    private int[] convert(String num) {
        boolean isA = true, neg = false;
        int a = 0, b = 0;
        for(int i = 0; i < num.length(); i++) {
            if(num.charAt(i) == '-')
                neg = true;
            else if(num.charAt(i) == '+' || num.charAt(i) == 'i') {
                if(isA && neg)
                    a *= -1;
                else if(!isA && neg)
                    b *= -1;
                neg = isA = false;
            }
            else if(isA)
                a = 10 * a + num.charAt(i) - '0';
            else
                b = 10 * b + num.charAt(i) - '0';
        }
        return new int[]{a, b};
    }
}
```
```JavaScript []
/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
var complexNumberMultiply = function(num1, num2) {
    convert = function(num) {
        let isA = true, neg = false, a = 0, b = 0
        for(let i = 0; i < num.length; i++)
            if(num.charAt(i) == '-')
                neg = true
            else if(num.charAt(i) == '+' || num.charAt(i) == 'i') {
                if(neg)
                    if(isA)
                        a *= -1
                    else
                        b *= -1
                isA = neg = false
            } else if(isA)
                a = 10 * a + num.charCodeAt(i) - '0'.charCodeAt(0)
            else
                b = 10 * b + num.charCodeAt(i) - '0'.charCodeAt(0)
        return [a, b]
    }

    const n1 = convert(num1), n2 = convert(num2)
    return "" + (n1[0] * n2[0] - n1[1] * n2[1]) + "+" + (n1[1] * n2[0] + n1[0] * n2[1]) + "i"
};
```
```Go []
func complexNumberMultiply(num1 string, num2 string) string {
    convert := func(num string) []int {
        isA, neg, a, b := true, false, 0, 0
        for i, r := range num {
            if num[i] == '-' {
                neg = true
            } else if num[i] == '+' || num[i] == 'i' {
                if neg {
                    if isA {
                        a *= -1
                    } else {
                        b *= -1
                    }
                }
                isA, neg = false, false
            } else if isA {
                a = 10 * a + int(r - rune('0'))
            } else {
                b = 10 * b + int(r - rune('0'))
            }
        }
        return []int{a, b}
    }
    n1, n2 := convert(num1), convert(num2)
    return fmt.Sprintf("%d+%di", n1[0] * n2[0] - n1[1] * n2[1], n1[1] * n2[0] + n1[0] * n2[1])
}
```