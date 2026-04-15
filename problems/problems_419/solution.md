# [Python/Java/JavaScript/Go] 边角统计 or 岛屿数量

> Author: Benhao
> Date: 2021-12-18
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
每个战舰都会有边角，有且仅有一个左上边角、右上边角、右下边角、左下边角。
具体来说，战舰里只有一个点，左边和上边都是'.'；只有一个点，上边和右边都是'.'；只有一个点，右边和下边都是'.'；只有一个点下边和左边都是'.'。
我们只需要任选一个边角，进行统计即可。

### 代码

```Python3 []
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        return sum(board[i][j] == 'X' and (i == 0 or board[i-1][j] == '.') and (j == 0 or board[i][j-1] == '.') for i in range(len(board)) for j in range(len(board[0])))
```
```Java []
class Solution {
    public int countBattleships(char[][] board) {
        int ans = 0;
        for(int i=0;i<board.length;i++)
            for(int j=0;j<board[0].length;j++)
                if(board[i][j] == 'X' && (i == 0 || board[i-1][j] == '.') && (j == 0 || board[i][j-1] == '.'))
                    ans++;
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {character[][]} board
 * @return {number}
 */
var countBattleships = function(board) {
    let ans = 0
    for(let i=0;i<board.length;i++)
        for(let j=0;j<board[0].length;j++)
            if(board[i][j] == 'X' && (i == 0 || board[i-1][j] == '.') && (j == 0 || board[i][j-1] == '.'))
                ans++
    return ans
};
```
```Go []
func countBattleships(board [][]byte) (ans int) {
    for i, row := range board {
        for j, cell := range row {
            if cell == 'X' && (i == 0 || board[i-1][j] == '.') && (j == 0 || board[i][j-1] == '.') {
                ans++
            }
        } 
    }
    return
}
```

当然这也是比较简单的一种岛屿统计，可以使用传统的dfs或bfs做
```python3
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] == '.':
                return False
            board[i][j] = '.'
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                dfs(i + dx, j + dy)
            return True
        
        return sum(dfs(i, j) for i in range(len(board)) for j in range(len(board[0])))
```