# [Python/Go/C] Repeated division

> Author: Benhao
> Date: 2024-02-27
> Upvotes: 1
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [12. 整数转罗马数字](https://leetcode.cn/problems/integer-to-roman/description/)

[TOC]

# Intuition

> Divide and take remainders from the largest place value to the smallest. For a digit of 4 or 9, pair the current symbol with the symbol for five or ten times its value. For a digit greater than 4, use the symbol for five times the value. Fill the remaining amount with copies of the current symbol.

# Approach

> Repeatedly divide until the number becomes 0. The divisors are 1000, 100, 10, and finally 1.



# Code
```Python3 []
trans = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
class Solution:
    def intToRoman(self, num: int) -> str:
        res = []
        d = 1000
        while num:
            cnts = num // d
            if cnts == 4 or cnts == 9:
                res.append(trans[d])
                res.append(trans[d * (cnts + 1)])
            elif cnts > 4:
                res.append(trans[5 * d])
                for i in range(cnts - 5):
                    res.append(trans[d])
            else:
                for i in range(cnts):
                    res.append(trans[d])
            num %= d
            d //= 10
        return ''.join(res)
```
```Go []
func trans(v int) byte {
    switch v {
        case 1:
            return 'I'
        case 5:
            return 'V'
        case 10:
            return 'X'
        case 50:
            return 'L'
        case 100:
            return 'C'
        case 500:
            return 'D'
        case 1000:
            return 'M'
    }
    return ' '
}

func intToRoman(num int) string {
    ans := []byte{}
    for d := 1000; num > 0; d /= 10 {
        if cnts := num / d; cnts == 4 || cnts == 9 {
            ans = append(ans, trans(d))
            ans = append(ans, trans((cnts + 1) * d))
        } else if cnts > 4 {
            ans = append(ans, trans(5 * d))
            for i := 0; i < cnts - 5; i++ {
                ans = append(ans, trans(d))
            }
        } else {
            for i := 0; i < cnts; i++ {
                ans = append(ans, trans(d))
            }            
        }
        num %= d
    }
    return string(ans)
}
```
```C []
char trans(int v) {
    switch (v) {
        case 1:
            return 'I';
        case 5:
            return 'V';
        case 10:
            return 'X';
        case 50:
            return 'L';
        case 100:
            return 'C';
        case 500:
            return 'D';
        case 1000:
            return 'M';
    }
    return ' ';
}
char* intToRoman(int num) {
    char *ans = malloc(sizeof(char) * 32);
    bzero(ans, 32);
    for (int idx = 0, d = 1000; num > 0; d /= 10) {
        int cnts = num / d;
        if (cnts == 4 || cnts == 9) {
            ans[idx++] = trans(d);
            ans[idx++] = trans((cnts + 1) * d);
        } else if (cnts > 4) {
            ans[idx++] = trans(5 * d);
            for (int i = 0; i < cnts - 5; i++) {
                ans[idx++] = trans(d);
            }
        } else {
            for (int i = 0; i < cnts; i++) {
                ans[idx++] = trans(d);
            }
        }
        num %= d;
    }
    return ans;
}
```
