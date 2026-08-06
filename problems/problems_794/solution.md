# [Python/Java/JavaScript/Go] 纯业务逻辑

> slug: pythonjavajavascriptgo-chun-ye-wu-luo-ji-20k3
> date: 2021-12-08
> tags: Go, Java, JavaScript, Python, Python3
> question: Valid Tic-Tac-Toe State (valid-tic-tac-toe-state)
> url: https://leetcode.cn/problems/valid-tic-tac-toe-state/solutions/ZS7wSR/pythonjavajavascriptgo-chun-ye-wu-luo-ji-20k3/

---
### 解题思路
X先手，所以个数要么比O多一个，要么一样。
两个人之间只能有一个人赢，赢的时候，X赢的话必然比O多一个，O赢的话必然和X一样多。

### 代码

```Python3 []
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x = o = xw = ow = 0
        for row in board:
            s = set(row)
            if len(s) == 1 and (t:=s.pop()) != ' ':
                if t == 'X':
                    xw += 1
                else:
                    ow += 1
            for c in row:
                if c == 'X':
                    x += 1
                elif c == 'O':
                    o += 1
        for c in range(len(board[0])):
            t = board[0][c]
            if t != " ":
                r = 0
                while r < len(board) and board[r][c] == t:
                    r += 1
                if r == len(board):
                    if t == "X":
                        xw += 1
                    else:
                        ow += 1
        mid = board[1][1]
        if mid != " ":
            if board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]:
                if mid == "X":
                    xw += 1
                else:
                    ow += 1
        if (x == o or x == o + 1) and not (xw and ow):
            if xw:
                return x == o + 1
            elif ow:
                return x == o
            return True
        return False
```
```Java []
class Solution {
    public boolean validTicTacToe(String[] board) {
        int x = 0, o = 0, res;
        for(int i=0;i<board.length;i++)
            for(int j=0;j<board[0].length();j++)
                if(board[i].charAt(j) == 'X')
                    x++;
                else if(board[i].charAt(j) == 'O')
                    o++;
        boolean xw = false, ow = false;
        for(int i=0;i<board.length;i++){
            res = isAllSame(i, 0, 0, 1, board);
            xw |= (res == 1);
            ow |= (res == -1);
            res = isAllSame(0, i, 1, 0, board);
            xw |= (res == 1);
            ow |= (res == -1);
        }
        res = isAllSame(0, 0, 1, 1, board);
        xw |= (res == 1);
        ow |= (res == -1);
        res = isAllSame(0, 2, 1, -1, board);
        xw |= (res == 1);
        ow |= (res == -1);
        if(xw && ow)
            return false;
        return (xw && x == o + 1) || (ow && x == o) || (!xw && !ow && (x == o || x == o + 1));
    }

    private int isAllSame(int r, int c, int dr, int dc, String[] board){
        char t = board[r].charAt(c);
        if(t != ' '){
            while(r >= 0 && c >= 0 && r < board.length && c < board[0].length() && board[r].charAt(c) == t){
                r += dr;
                c += dc;
            }
            if((dr > 0 && r == board.length) || (dc > 0 && c == board[0].length()))
                return t == 'X' ? 1 : -1;
        }
        return 0;
    }
}
```
```JavaScript []
/**
 * @param {string[]} board
 * @return {boolean}
 */
var validTicTacToe = function(board) {
    isAllSame = function(r,c,dr,dc){
        const t = board[r].charAt(c)
        if(t != ' '){
            while(r >= 0 && c >= 0 && r < board.length && c < board[0].length && board[r].charAt(c) == t){
                r += dr
                c += dc
            }
            if((dr > 0 && r == board.length) || (dc > 0 && c == board[0].length))
                return t == 'X' ? 1 : -1
        }
        return 0
    }
    let x = 0, o = 0, res
    for(let i=0;i<board.length;i++)
        for(let j=0;j<board[0].length;j++)
            if(board[i].charAt(j) == 'X')
                x++
            else if(board[i].charAt(j) == 'O')
                o++
    let xw = false, ow = false
    for(let i=0;i<board.length;i++){
        res = isAllSame(i, 0, 0, 1)
        xw |= (res == 1)
        ow |= (res == -1)
        res = isAllSame(0, i, 1, 0)
        xw |= (res == 1)
        ow |= (res == -1)
    }
    res = isAllSame(0, 0, 1, 1)
    xw |= (res == 1)
    ow |= (res == -1)
    res = isAllSame(0, 2, 1, -1);
    xw |= (res == 1);
    ow |= (res == -1);
    if(xw && ow)
        return false;
    return (xw && x == o + 1) || (ow && x == o) || (!xw && !ow && (x == o || x == o + 1));
};
```
```Go []
func validTicTacToe(board []string) bool {
    isAllSame := func(r,c,dr,dc int) int {
        t := board[r][c]
        if t != ' '{
            for r >= 0 && c >= 0 && r < len(board) && c < len(board[0]) && board[r][c] == t {
                r += dr
                c += dc
            }
            if (dr > 0 && r ==len(board)) || (dc > 0 && c == len(board[0])) {
                if t == 'X' {
                    return 1
                } else{ 
                    return -1
                }
            }
        }
        return 0
    }

    x, o, res := 0, 0, 0
    for i:=0; i<len(board); i++{
        for j:=0; j<len(board[0]);j++ {
            if board[i][j] == 'X'{
                x++
            } else if board[i][j] == 'O'{
                o++
            }
        }
    }
    xw, ow := false, false
    for i := 0; i<len(board);i++ {
        res = isAllSame(i, 0, 0, 1)
        xw = xw || (res == 1)
        ow = ow || (res == -1)
        res = isAllSame(0, i, 1, 0)
        xw = xw || (res == 1)
        ow = ow || (res == -1)
    }
    res = isAllSame(0, 0, 1, 1)
    xw = xw || (res == 1)
    ow = ow || (res == -1)
    res = isAllSame(0, 2, 1, -1)
    xw = xw || (res == 1)
    ow = ow || (res == -1)
    if xw && ow {
        return false
    }
    return (xw && x == o + 1) || (ow && x == o) || (!xw && !ow && (x == o || x == o + 1))
}
```