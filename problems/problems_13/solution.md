# [Python/Go/C] 模拟

> Author: Benhao
> Date: 2024-02-27
> Upvotes: 0
> Tags: C, Go, Java, Python3, TypeScript

---


> Problem: [13. 罗马数字转整数](https://leetcode.cn/problems/roman-to-integer/description/)

[TOC]

# 思路

> 注意到从右至左是递增的话是加法，出现逆序的地方是减法

# 解题方法

> 转换罗马数字比较相邻大小决定正负

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(1)$



# Code
```Python3 []
trans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,}
class Solution:
    def romanToInt(self, s: str) -> int:
        ans, last = 0, 0
        for c in s[::-1]:
            val = trans[c]
            if val < last:
                ans -= val
            else:
                ans += val
            last = val
        return ans
```
```Go []
func trans(r byte) int {
    switch r {
        case 'I':
            return 1
        case 'V':
            return 5
        case 'X':
            return 10
        case 'L':
            return 50
        case 'C':
            return 100
        case 'D':
            return 500
        case 'M':
            return 1000
    }
    return 0
}
func romanToInt(s string) (ans int) {
    for i, last := len(s) - 1, 0; i >= 0; i-- {
        v := trans(s[i])
        if v < last {
            ans -= v
        } else {
            ans += v
        }
        last = v
    }
    return
}
```
```C []
int trans(char r) {
    switch (r) {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
    }
    return 0;
}

int romanToInt(char* s) {
    int ans = 0;
    for (int i = strlen(s) - 1, last = 0; i >= 0; i--) {
        int v = trans(s[i]);
        if (v < last) {
            ans -= v;
        } else {
            ans += v;
        }
        last = v;
    }
    return ans;
}
```
