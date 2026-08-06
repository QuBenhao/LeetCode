# [Python/Go/C] 转向模拟

> slug: pythongoc-zhuan-xiang-mo-ni-by-himymben-rani
> date: 2024-02-28
> tags: C, Go, Java, Python3, TypeScript
> question: Zigzag Conversion (zigzag-conversion)
> url: https://leetcode.cn/problems/zigzag-conversion/solutions/XsE8LL/pythongoc-zhuan-xiang-mo-ni-by-himymben-rani/

---

> Problem: [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/description/)

[TOC]

# 思路

> 类似x,y坐标题目中，下次移动的方向，走到头转向。只不过这里是一维的，在达到行数后转向

# 解题方法

> 模拟当前处于哪行，先填入那行，后面再将所有行的答案合并

# 复杂度

时间复杂度:
> $O(n)$

空间复杂度:
> $O(n)$



# Code
```Python3 []
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        res = ['' for _ in range(numRows)]
        idx, dirc = 0, -1
        for c in s:
            res[idx] += c
            if not idx or idx == numRows - 1:
                dirc *= -1
            idx += dirc
        return "".join(res)
```
```Go []
func convert(s string, numRows int) string {
    if len(s) <= numRows || numRows == 1 {
        return s
    }
    res := [][]byte{}
    for i := 0; i < numRows; i++ {
        res = append(res, []byte{})
    }
    for i, row, dir := 0, 0, -1; i < len(s); i++ {
        res[row] = append(res[row], s[i])
        if row == 0 || row == numRows - 1 {
            dir *= -1
        }
        row += dir
    }
    ans := []byte{}
    for i := 0; i < numRows; i++ {
        ans = append(ans, res[i]...)
    }
    return string(ans)
}
```
直接依次计算每行的下一个在原字符串中的坐标
```C []
char* convert(char* s, int numRows) {
    int n = strlen(s);
    if (n <= numRows || numRows == 1) {
        return strdup(s);
    }
    char *ans = malloc(sizeof(char) * (n + 1));
    bzero(ans, sizeof(char) * (n + 1));
    for (int i = 0, idx = 0; i < numRows; i++) {
        for (int j = i, cur = 0; j < n; cur ^= 1) {
            ans[idx++] = s[j];
            if (i == 0 || i == numRows - 1) {
                j += numRows * 2 - 2;
            } else {
                j += cur == 0 ? (numRows - 1 - i) * 2 : i * 2;
            }
        }
    }
    return ans;
}
```
