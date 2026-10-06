# [Python/Go] Dynamic programming

> Author: Benhao
> Date: 2022-02-18
> Upvotes: 1
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
For each new row, add the previous row's preceding column to each column's value. Update from right to left.

### Code

```Python3 []
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1] + [0] * rowIndex
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                dp[j] += dp[j - 1]
        return dp
```
```Go []
func getRow(rowIndex int) []int {
    dp := make([]int, rowIndex + 1)
    dp[0] = 1
    for i := 1; i <= rowIndex; i++ {
        for j := i; j > 0; j-- {
            dp[j] += dp[j - 1]
        }
    }
    return dp
}
```
