# [Python/Java/JavaScript/Go] 多源BFS

> Author: Benhao
> Date: 2022-01-29
> Upvotes: 26
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
本题可以存在多个水域作为BFS的起点，是多源BFS的模板题。可以用原矩阵进行标记访问过(更新答案)。

### 代码

```Python3 []
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue, m, n, cost = [], len(isWater), len(isWater[0]), 0
        for i, row in enumerate(isWater):
            for j, val in enumerate(row):
                # 水域，作为起点入队，并更新为答案需要返回的0
                if val:
                    isWater[i][j] = 0
                    queue.append((i, j))
                # 陆地：先更新为无限大的高度，等BFS时更新它
                else:
                    isWater[i][j] = inf
        while queue:
            nxt = []
            cost += 1
            for i, j in queue:
                for dx, dy in (0, 1), (1, 0), (-1, 0), (0, -1):
                    # 只有没被更新过的陆地才能被更新，否则已经有更近的水域访问过它了
                    if 0 <= (nx := i + dx) < m and 0 <= (ny := j + dy) < n and isWater[nx][ny] > cost:
                        isWater[nx][ny] = cost
                        nxt.append((nx, ny))
            queue = nxt
        return isWater
```
```Java []
class Solution {
    private static final int MAX = 0x3f3f3f;
    private static final int[][] DIRS = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    public int[][] highestPeak(int[][] isWater) {
        int m = isWater.length, n = isWater[0].length;
        Deque<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                if(isWater[i][j] == 1){
                    queue.offerLast(i * n + j);
                    isWater[i][j] = 0;
                } else
                    isWater[i][j] = MAX;
        int cost = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            cost++;
            for(int i=0;i<size;i++){
                int point = queue.pollFirst();
                int x = point/n, y = point%n;
                for(int[] dir: DIRS){
                    int nx = x + dir[0], ny = y + dir[1];
                    if(nx >= 0 && ny >= 0 && nx < m && ny < n && isWater[nx][ny] > cost){
                        isWater[nx][ny] = cost;
                        queue.offerLast(nx * n + ny);
                    }
                }
            }
        }
        return isWater;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */
const DIRS = [[1, 0], [0, 1], [0, -1], [-1, 0]], MAX = 0x3f3f3f
var highestPeak = function(isWater) {
    const m = isWater.length, n = isWater[0].length
    let queue = new Array(), cost = 0
    for(let i = 0; i < m; i++)
        for(let j = 0; j < n; j++)
            if(isWater[i][j] == 1){
                isWater[i][j] = 0
                queue.push([i, j])
            }else{
                isWater[i][j] = MAX
            }
    while(queue.length > 0){
        const nxt = new Array()
        cost++
        for(const point of queue)
            for(const dir of DIRS){
                const nx = point[0] + dir[0], ny = point[1] + dir[1]
                if(nx >= 0 && ny >= 0 && nx < m && ny < n && isWater[nx][ny] > cost){
                    isWater[nx][ny] = cost
                    nxt.push([nx, ny])
                }
            }
        queue = nxt
    }
    return isWater
};
```
```Go []
const MAX int = 0x3f3f3f
func highestPeak(isWater [][]int) [][]int {
    m, n, queue, dirs := len(isWater), len(isWater[0]), [][]int{}, [][]int{{1, 0}, {0, 1}, {0, -1}, {-1, 0}}
    for i := 0; i < m; i++{
        for j := 0; j < n; j++{
            if isWater[i][j] == 1{
                isWater[i][j] = 0
                queue = append(queue, []int{i, j})
            } else{
                isWater[i][j] = MAX
            }
        }
    }
    for cost := 1; len(queue) > 0; cost++{
        size := len(queue)
        for i := 0; i < size; i++{
            point := queue[0]
            queue = queue[1:]
            for _, dir := range dirs{
                nx, ny := point[0] + dir[0], point[1] + dir[1]
                if nx >= 0 && ny >= 0 && nx < m && ny < n && isWater[nx][ny] > cost{
                    isWater[nx][ny] = cost
                    queue = append(queue, []int{nx, ny})
                }
            }
        }
    }
    return isWater
}
```