# [Python/Go] Brute-force DFS or BFS with pruning

> slug: python-chun-bao-li-dfswei-you-hua-by-him-uk9z
> date: 2021-11-08
> tags: Go, Python, Python3
> question: Zuma Game (zuma-game)
> url: https://leetcode.cn/problems/zuma-game/solutions/jSkoSf/python-chun-bao-li-dfswei-you-hua-by-him-uk9z/

---
### Approach
DFS checks whether the board is empty and enumerates ball colors and insertion positions. in_a_row detects and removes runs of three or more.

### Code

```python3
COLORS = ["R", "Y", "B", "G", "W"]
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # Return -1 if any board color still has fewer than three balls after including the hand
        cnts, cnts_b = Counter(hand), Counter(board)
        total = len(hand)
        if any(cnts_b[k] + cnts[k] < 3 for k in cnts_b.keys()):
            return -1

        @lru_cache(None)
        def dfs(bd, hd):
            # All balls are removed; return the number used
            if len(bd) <= 0:
                return total - sum(hd)
            n = len(bd)
            ans = inf
            # Iterate over the colors in hand
            for i, v in enumerate(hd):
                # If a ball of this color remains
                if v:
                    cp = list(hd)
                    # Use this ball
                    cp[i] -= 1
                    nt = tuple(cp)
                    # Enumerate insertion positions
                    for j in range(n + 1):
                        ans = min(ans, dfs(in_a_row(bd[:j] + COLORS[i] + bd[j:]), nt))
            return ans
        
        @lru_cache(None)
        def in_a_row(bd):
            l = r = 0
            while l < len(bd):
                # If at least three consecutive balls match, remove bd[l:r] and recursively return the cleaned board
                while r < len(bd) and bd[r] == bd[l]:
                    r += 1
                if r - l > 2:
                    return in_a_row(bd[:l] + bd[r:])
                l = r
            return bd

        # Pass the hand as a tuple of color counts to avoid trying duplicate balls
        start = [cnts[c] for c in COLORS]
        res = dfs(board, tuple(start))
        return res if res != inf else -1
```
BFS with pruning should be the most efficient approach (adapted from [@ChangXingJiang](/u/changxingjiang/)).
```Python3 []
COLORS = ["R", "Y", "B", "G", "W"]
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @lru_cache(None)
        def clean(s):
            # Remove all runs that should disappear from the board
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        cnts = Counter(hand)
        start = [cnts[c] for c in COLORS]
        hand = tuple(start)

        # Initialize a deque of states: current board, current hand, and number of turns
        queue = deque([(board, hand, 0)])

        # Memoization
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i in range(len(cur_board) + 1):
                for j in range(len(cur_hand)):
                    if not cur_hand[j]:
                        continue
                    c = COLORS[j]
                    # Pruning rule 1: insert only at the start of a run of the same color (other positions in that run are equivalent)
                    if i > 0 and cur_board[i - 1] == c:
                        continue

                    # Pruning rule 2: insert a ball only in either of these cases
                    #  - Case 1: the neighboring balls have the same color, different from the inserted ball
                    #  - Case 2: the inserted ball matches the following ball
                    choose = False
                    if 0 < i < len(cur_board) and cur_board[i - 1] == cur_board[i] and cur_board[i - 1] != c:
                        choose = True
                    if i < len(cur_board) and cur_board[i] == c:
                        choose = True

                    if choose:
                        cp = list(cur_hand)
                        cp[j] -= 1
                        b2, h2 = clean(cur_board[:i] + c + cur_board[i:]), tuple(cp)
                        if not b2:
                            return step + 1
                        if (b2, h2) not in visited:
                            queue.append((b2, h2, step + 1))
                            visited.add((b2, h2))
                            visited.add((b2[::-1], h2))

        return -1
```
```Go []
type state struct {
    board string
    hand [5]int
}

func findMinStep(board string, hand string) int {
    cache := map[string]string{}
    COLORS := "RYBGW"

    var clean func(b string) string
    clean = func(board string) string {
        if v, ok := cache[board]; ok {
            return v
        } 
        res := board
        for i, j := 0, 0; i < len(board); {
            for j < len(board) && board[i] == board[j] {
                j += 1
            }
            if j - i > 2 {
                res = clean(board[:i] + board[j:])
                cache[board] = res
                return res
            }
            i = j
        }
        cache[board] = res
        return res
    }

    cnts := func(hand string) [5]int {
        res := [5]int{}
        for i := 0; i < len(hand); i++ {
            for j, c := range COLORS {
                if hand[i] == byte(c) {
                    res[j]++
                    break
                }
            }
        }
        return res
    }

    queue := make([]state, 0, 6)
    init := state{board, cnts(hand)}
    queue = append(queue, init)
    visited := map[state]int{}
    visited[init] = 0
    for len(queue) > 0 {
        curState := queue[0]
        cur_board, cur_hand := curState.board, curState.hand
        if len(cur_board) == 0 {
            return visited[curState]
        }
        queue = queue[1:]
        for i := 0; i <= len(cur_board) ; i++ {
            for j, r := range COLORS {
                if cur_hand[j] > 0 {
                    c := byte(r)
                    // Pruning rule 1: insert only at the start of a run of the same color (other positions in that run are equivalent)
                    if i > 0 && cur_board[i - 1] == c{
                        continue
                    }

                    /** 
                     *  Pruning rule 2: insert a ball only in either of these cases
                     *  - Case 1: the neighboring balls have the same color, different from the inserted ball
                     *  - Case 2: the inserted ball matches the following ball
                     */
                    choose := false
                    if 0 < i && i < len(cur_board) && cur_board[i - 1] == cur_board[i] && cur_board[i - 1] != c{
                        choose = true
                    }
                    if i < len(cur_board) && cur_board[i] == c{
                        choose = true
                    }
                    
                    if choose {
                        nxt := [5]int{}
                        for k,_ := range COLORS{
                            nxt[k] = cur_hand[k]
                        }
                        nxt[j] -= 1
                        
                        nextState := state{clean(cur_board[:i] + string(c) + cur_board[i:]), nxt}
                        if _,ok := visited[nextState]; !ok {
                            queue = append(queue, nextState)
                            visited[nextState] = visited[curState] + 1
                        }
                    }
                }
            }
        }
    }
    return -1
}
```
