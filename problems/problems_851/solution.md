# [Python/Java/JavaScript/Go] 记忆化递归 or 拓扑bfs

> slug: pythonjavajavascriptgo-ji-yi-hua-di-gui-eod8m
> date: 2021-12-14
> tags: Go, Java, JavaScript, Python, Python3
> question: Loud and Rich (loud-and-rich)
> url: https://leetcode.cn/problems/loud-and-rich/solutions/7JaxWq/pythonjavajavascriptgo-ji-yi-hua-di-gui-eod8m/

---
### 解题思路
根据大小关系建图，每个人可以连接所有比自己有钱的人，这样搜每个人就可以搜索出所有比他有钱的人，然后返回在这些人里最安静的那个人作为这个人的答案。
记忆化可以避免重复搜索同样的人，实现 优化。

### 代码

```Python3
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        connect, KEY = defaultdict(set), lambda y:quiet[y]
        for a,b in richer:
            connect[b].add(a)
        @lru_cache(None)
        def dfs(x):
            return x if not connect[x] else min((x, min((dfs(o) for o in connect[x]), key=KEY)), key=KEY)
        return [dfs(i) for i in range(len(quiet))]
```
```Python3 []
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        connect = defaultdict(set)
        for a,b in richer:
            connect[b].add(a)

        @lru_cache(None)
        def dfs(x):
            ans = x
            for other in connect[x]:
                if quiet[dfs(other)] < quiet[ans]:
                    ans = dfs(other)
            return ans

        return [dfs(i) for i in range(len(quiet))]
```
```Java []
class Solution {
    private Map<Integer, Set<Integer>> connect;
    private int[] ans;
    private int[] quiet;
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        connect = new HashMap<>();
        ans = new int[quiet.length];
        this.quiet = quiet;
        for(int i=0;i<quiet.length;i++)
            ans[i] = -1;
        for(int[] r: richer) {
            Set<Integer> l = connect.getOrDefault(r[1], new HashSet<>());
            l.add(r[0]);
            connect.put(r[1], l);
        }
        for(int i=0;i<quiet.length;i++)
            dfs(i);
        return ans;
    }

    private int dfs(int x) {
        if(ans[x] != -1)
            return ans[x];
        ans[x] = x;
        if(!connect.containsKey(x))
            return ans[x];
        for(int other: connect.get(x))
            if(quiet[dfs(other)] < quiet[ans[x]])
                ans[x] = dfs(other);
        return ans[x];
    }
}
```
```JavaScript []
/**
 * @param {number[][]} richer
 * @param {number[]} quiet
 * @return {number[]}
 */
var loudAndRich = function(richer, quiet) {
    const connect = new Map()
    for(const r of richer){
        if(connect.has(r[1]))
            connect.get(r[1]).add(r[0])
        else
            connect.set(r[1], new Set([r[0]]))
    }
    const ans = new Array(quiet.length)
    ans.fill(-1)
    
    var dfs = function(x) {
        if(ans[x] >= 0)
            return ans[x]
        ans[x] = x
        if(!connect.has(x))
            return ans[x]
        for(const other of connect.get(x))
            if(quiet[dfs(other)] < quiet[ans[x]])
                ans[x] = dfs(other)
        return ans[x]
    }
    for(let i=0;i<quiet.length;i++)
        dfs(i)
    return ans
};
```
```Go []
func loudAndRich(richer [][]int, quiet []int) []int {
    connect, ans := map[int][]int{}, make([]int, len(quiet))
    for _, r := range(richer){
        if v, err := connect[r[1]]; !err{
            connect[r[1]] = []int{r[0]}
        } else {
            connect[r[1]] = append(v, r[0])
        }
    }
    for i := range ans {
        ans[i] = -1
    }
    var dfs func(x int) int
    dfs = func(x int) int {
        if ans[x] >= 0 {
            return ans[x]
        }
        ans[x] = x
        if v, err := connect[x]; !err {
            return ans[x]
        } else {
            for _, other := range v{
                if quiet[dfs(other)] < quiet[ans[x]] {
                    ans[x] = dfs(other)
                }
            }
        }
        return ans[x]
    }
    for i := range quiet {
        dfs(i)
    }
    return ans
}
```
这题可以从最有钱的人开始，也就是入度为0的点进行拓扑排序，这样每次遍历过的人都是比当前有钱的，我们只需要比较当前和之前的答案即可知道当前的答案了。
```Python3 []
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        connect, degree, ans = defaultdict(list), [0] * len(quiet), [i for i in range(len(quiet))]
        for u, v in richer:
            connect[u].append(v)
            degree[v] += 1
        queue = deque([i for i in range(len(degree)) if not degree[i]])
        while queue:
            u = queue.popleft()
            for v in connect[u]:
                if quiet[ans[u]] < quiet[ans[v]]:
                    ans[v] = ans[u]
                degree[v] -= 1
                if not degree[v]:
                    queue.append(v)
        return ans
```
```Java []
class Solution {
    public int[] loudAndRich(int[][] richer, int[] quiet) {
        Map<Integer, List<Integer>> connect = new HashMap<>();
        int[] degree = new int[quiet.length], ans = new int[quiet.length];
        for(int i=0;i<quiet.length;i++)
            ans[i] = i;
        for(int[] r: richer){
            List<Integer> l = connect.getOrDefault(r[0], new ArrayList<>());
            l.add(r[1]);
            connect.put(r[0], l);
            degree[r[1]]++;
        }
        Deque<Integer> queue = new LinkedList<>();
        for(int i=0;i<quiet.length;i++)
            if(degree[i] == 0)
                queue.offerLast(i);
        while(!queue.isEmpty()){
            int u = queue.pollFirst();
            if(connect.containsKey(u))
                for(int v: connect.get(u)){
                    if(quiet[ans[u]] < quiet[ans[v]])
                        ans[v] = ans[u];
                    degree[v]--;
                    if(degree[v] == 0)
                        queue.offerLast(v);
                }
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} richer
 * @param {number[]} quiet
 * @return {number[]}
 */
var loudAndRich = function(richer, quiet) {
    const connect = new Map(), degree = new Array(quiet.length),ans = new Array(quiet.length)
    degree.fill(0)
    for(const r of richer){
        if(connect.has(r[0]))
            connect.get(r[0]).push(r[1])
        else
            connect.set(r[0],[r[1]])
        degree[r[1]]++
    }
    const queue = []
    for(let i=0;i<quiet.length;i++){
        ans[i] = i
        if(degree[i]==0)
            queue.push(i)
    }
    while(queue.length > 0){
        const u = queue.shift()
        if(connect.has(u))
            for(const v of connect.get(u)){
                if(quiet[ans[u]] < quiet[ans[v]])
                    ans[v] = ans[u]
                degree[v]--
                if(degree[v] == 0)
                    queue.push(v)
            }
    }
    return ans
};
```
```Go []
func loudAndRich(richer [][]int, quiet []int) []int {
    connect, degree, ans := map[int][]int{}, make([]int, len(quiet)), make([]int, len(quiet))
    for _, r := range(richer){
        if v, err := connect[r[0]]; !err{
            connect[r[0]] = []int{r[1]}
        } else {
            connect[r[0]] = append(v, r[1])
        }
        degree[r[1]]++
    }
    queue := []int{}
    for i := range ans {
        ans[i] = i
        if degree[i] == 0 {
            queue = append(queue, i)
        }
    }
    for len(queue) > 0{
        u := queue[0]
        queue = queue[1:]
        if list, err := connect[u]; err {
            for _, v := range list {
                if quiet[ans[u]] < quiet[ans[v]] {
                    ans[v] = ans[u]
                }
                degree[v]--
                if degree[v] == 0 {
                    queue = append(queue, v)
                }
            }
        }
    }
    return ans
}
```