# [Python/Go] 纯暴力dfs 或 BFS剪枝

> slug: python-chun-bao-li-dfswei-you-hua-by-him-uk9z
> date: 2021-11-08
> tags: Go, Python, Python3
> question: Zuma Game (zuma-game)
> url: https://leetcode.cn/problems/zuma-game/solutions/jSkoSf/python-chun-bao-li-dfswei-you-hua-by-him-uk9z/

---
### 解题思路
dfs就是枚举有没有把棋盘消灭光、枚举不同颜色球和不同的插入位置，in_a_row就是检测有没有三连并消元。

### 代码

```python3
COLORS = ["R", "Y", "B", "G", "W"]
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # 单纯检测一下board里有没有加上手上的还不能够3个的球，直接返回-1
        cnts, cnts_b = Counter(hand), Counter(board)
        total = len(hand)
        if any(cnts_b[k] + cnts[k] < 3 for k in cnts_b.keys()):
            return -1

        @lru_cache(None)
        def dfs(bd, hd):
            # 全部消掉了，返回所用的球数
            if len(bd) <= 0:
                return total - sum(hd)
            n = len(bd)
            ans = inf
            # 遍历手上的球的颜色
            for i, v in enumerate(hd):
                # 如果该颜色还有球可以用
                if v:
                    cp = list(hd)
                    # 用掉这个球
                    cp[i] -= 1
                    nt = tuple(cp)
                    # 枚举插入位置
                    for j in range(n + 1):
                        ans = min(ans, dfs(in_a_row(bd[:j] + COLORS[i] + bd[j:]), nt))
            return ans
        
        @lru_cache(None)
        def in_a_row(bd):
            l = r = 0
            while l < len(bd):
                # 判断有没有连续三个一样的球，有的话就剪掉bd[l:r]，迭代返回
                while r < len(bd) and bd[r] == bd[l]:
                    r += 1
                if r - l > 2:
                    return in_a_row(bd[:l] + bd[r:])
                l = r
            return bd

        # 手上的以不同颜色的球计数的tuple作为传参，直接避免尝试重复的球
        start = [cnts[c] for c in COLORS]
        res = dfs(board, tuple(start))
        return res if res != inf else -1
```
应该用BFS+剪枝达到的最高效率(参考自[@ChangXingJiang](/u/changxingjiang/))
```Python3 []
COLORS = ["R", "Y", "B", "G", "W"]
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        @lru_cache(None)
        def clean(s):
            # 消除桌面上需要消除的球
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        cnts = Counter(hand)
        start = [cnts[c] for c in COLORS]
        hand = tuple(start)

        # 初始化用双端队列维护的状态队列：其中的三个元素分别为当前桌面的球、当期手中的球、当前回合数
        queue = deque([(board, hand, 0)])

        # 记忆化
        visited = {(board, hand)}

        while queue:
            cur_board, cur_hand, step = queue.popleft()
            for i in range(len(cur_board) + 1):
                for j in range(len(cur_hand)):
                    if not cur_hand[j]:
                        continue
                    c = COLORS[j]
                    # 第 1 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球(在它前面插入过了，不需要再插入，意义相同)
                    if i > 0 and cur_board[i - 1] == c:
                        continue

                    # 第 2 个剪枝条件: 只在以下两种情况放置新球
                    #  - 第 1 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                    #  - 第 2 种情况 : 当前球颜色与后面的球的颜色相同
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
                    // 第 1 个剪枝条件: 只在连续相同颜色的球的开头位置插入新球(在它前面插入过了，不需要再插入，意义相同)
                    if i > 0 && cur_board[i - 1] == c{
                        continue
                    }

                    /** 
                     *  第 2 个剪枝条件: 只在以下两种情况放置新球
                     *  - 第 1 种情况 : 当前后颜色相同且与当前颜色不同时候放置球
                     *  - 第 2 种情况 : 当前球颜色与后面的球的颜色相同
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