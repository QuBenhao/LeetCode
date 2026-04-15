# [Python/Go] 动态规划

> Author: Benhao
> Date: 2022-02-17
> Upvotes: 8
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
下一行杨辉三角由上一行杨辉三角得到

### 代码

```Python3 []
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]]
        for i in range(1, numRows):
            dp.append(dp[-1] + [1])
            for j in range(1, len(dp[-1]) - 1):
                dp[-1][j] = dp[-2][j - 1] + dp[-2][j]
        return dp
```
```Java []
class Solution {
    private static final List<List<Integer>> lists = new ArrayList<>();
    static {
        lists.add(new ArrayList<>(){{add(1);}});
        for(int i = 2; i <= 30; i++) {
            List<Integer> nextRow = new ArrayList<>(), lastRow = lists.get(lists.size() - 1);
            nextRow.add(1);
            for(int j = 1; j < lastRow.size(); j++)
                nextRow.add(lastRow.get(j - 1) + lastRow.get(j));
            nextRow.add(1);
            lists.add(nextRow);
        }
    }
    public List<List<Integer>> generate(int numRows) {
        return lists.subList(0, numRows);
    }
}
```
```JavaScript []
/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    const dp  = new Array()
    dp.push([1])
    for(let i = 1; i < numRows; i++) {
        const nextRow = new Array(), lastRow = dp[dp.length - 1]
        nextRow.push(1)
        for(let j = 1; j < lastRow.length; j++)
            nextRow.push(lastRow[j - 1] + lastRow[j])
        nextRow.push(1)
        dp.push(nextRow)
    }
    return dp
};
```
```Go []
func generate(numRows int) [][]int {
    ans := [][]int{{1}}
    for i := 1; i < numRows; i++ {
        lastRow, nextRow := ans[len(ans) - 1], make([]int, i + 1)
        nextRow[0], nextRow[i] = 1, 1
        for j := 1; j < i; j++ {
            nextRow[j] = lastRow[j - 1] + lastRow[j]
        }
        ans = append(ans, nextRow)
    }
    return ans
}
```