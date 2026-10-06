# [Python/Java/JavaScript/Go] Count corners or count islands

> Author: Benhao
> Date: 2021-12-18
> Upvotes: 17
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Each battleship has exactly one top-left, top-right, bottom-right, and bottom-left corner.
Specifically, exactly one cell has '.' both above and to the left; one has '.' above and to the right; one has '.' to the right and below; and one has '.' below and to the left.
Choose any one corner type and count it.

### Code

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

This is also a simple island-counting problem that can be solved with standard DFS or BFS.
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
