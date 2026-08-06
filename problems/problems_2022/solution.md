# [Python/Java/JavaScript/Go]  模拟 & 新年快乐！

> slug: pythonjavajavascriptgo-mo-ni-xin-nian-ku-qwcw
> date: 2021-12-31
> tags: Go, Java, JavaScript, Python, Python3
> question: Convert 1D Array Into 2D Array (convert-1d-array-into-2d-array)
> url: https://leetcode.cn/problems/convert-1d-array-into-2d-array/solutions/jA1Ysr/pythonjavajavascriptgo-mo-ni-xin-nian-ku-qwcw/

---
### 解题思路
都2022年了，一些2021年的评论我还看不到呢哈哈哈。大家新年快乐

### 代码

```python3 []
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [[original[i * n + j] for j in range(n)] for i in range(m)] if m * n == len(original) else []
```
```Java []
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        if(m * n != original.length)
            return new int[0][0];
        int[][] res = new int[m][n];
        for(int i=0;i<original.length;i++)
            res[i/n][i%n] = original[i];
        return res;
    }
}
```
```JavaScript []
/**
 * @param {number[]} original
 * @param {number} m
 * @param {number} n
 * @return {number[][]}
 */
var construct2DArray = function(original, m, n) {
    if(m * n != original.length)
        return []
    const res = new Array(m)
    for(let i=0;i<m;i++){
        res[i] = new Array(n)
        for(let j=0;j<n;j++)
            res[i][j] = original[i * n + j]
    }
    return res
};
```
```Go []
func construct2DArray(original []int, m int, n int) [][]int {
    if m * n != len(original) {
        return nil
    }
    res := make([][]int, m)
    for i:=0;i<m;i++{
        res[i] = make([]int, n)
        for j:=0;j<n;j++{
            res[i][j] = original[i * n + j]
        }
    }
    return res
}
```