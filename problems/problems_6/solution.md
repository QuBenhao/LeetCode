# [Python/Go/C] Simulate direction changes

> slug: pythongoc-zhuan-xiang-mo-ni-by-himymben-rani
> date: 2024-02-28
> tags: C, Go, Java, Python3, TypeScript
> question: Zigzag Conversion (zigzag-conversion)
> url: https://leetcode.cn/problems/zigzag-conversion/solutions/XsE8LL/pythongoc-zhuan-xiang-mo-ni-by-himymben-rani/

---

> Problem: [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/description/)

[TOC]

# Intuition

> As in problems with x,y coordinates, track the next direction of movement and turn at the end. Here the movement is one-dimensional, turning when the row limit is reached.

# Approach

> Simulate the current row and place the character there, then combine the results from all rows.

# Complexity

Time complexity:
> $O(n)$

Space complexity:
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
Directly calculate each row's next index in the original string.
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
