# [Python/Java/JavaScript] Dijkstra + 优先队列

> Author: Benhao
> Date: 2021-11-03
> Upvotes: 10
> Tags: Java, JavaScript, Python, Python3

---

### 解题思路
[三叶的题解](https://leetcode.cn/problems/trapping-rain-water-ii/solution/gong-shui-san-xie-jing-dian-dijkstra-yun-13ik/)
大致思路就是以边界为起点，从最低开始往内推，保留最高的边界高度（或本身是个边界）。
因为优先队列保证了每次第一次访问到一个点，一定是该点能存的雨水的最高高度了（它是后面所有高度最矮的）。

### 代码

```Python3 []
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n, ans = len(heightMap), len(heightMap[0]), 0
        visited, dirs, pq = [[False] * n for _ in range(m)], [(0,1),(1,0),(0,-1),(-1,0)], []
        for i in range(1,n-1):
            heapq.heappush(pq,(heightMap[0][i], 0, i))
            heapq.heappush(pq,(heightMap[m-1][i], m-1, i))
        for i in range(1,m-1):
            heapq.heappush(pq, (heightMap[i][0], i, 0))
            heapq.heappush(pq, (heightMap[i][n-1], i, n-1))
        while pq:
            h, x, y = heapq.heappop(pq)
            for dx, dy in dirs:
                nx, ny = x+dx,y+dy
                if 0 < nx < m - 1 and 0 < ny < n - 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    ans += max(0, h - heightMap[nx][ny])
                    heapq.heappush(pq, (max(h, heightMap[nx][ny]), nx, ny))
        return ans
```
```Java []
class Solution {
    public int trapRainWater(int[][] heightMap) {
        int m = heightMap.length, n = heightMap[0].length, ans = 0;
        PriorityQueue<int[]> q = new PriorityQueue<>((a,b)->a[2]-b[2]);
        int[][] dirs = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
        boolean[][] vis = new boolean[m][n];
        for (int i = 1; i < n-1; i++) {
            q.add(new int[]{0, i, heightMap[0][i]});
            q.add(new int[]{m - 1, i, heightMap[m - 1][i]});
        }
        for (int i = 1; i < m-1; i++) {
            q.add(new int[]{i, 0, heightMap[i][0]});
            q.add(new int[]{i, n - 1, heightMap[i][n-1]});
        }
        while(!q.isEmpty()){
            int[] cur = q.poll();
            for(int[] dir:dirs){
                int nx = dir[0] + cur[0], ny = dir[1] + cur[1];
                if(nx > 0 && nx < m - 1 && ny > 0 && ny < n - 1 && !vis[nx][ny]){
                    vis[nx][ny] = true;
                    ans += Math.max(0, cur[2] - heightMap[nx][ny]);
                    q.add(new int[]{nx, ny, Math.max(heightMap[nx][ny], cur[2])});
                }
            }
        }
        return ans;
    }
}
```
```JavaScript []
class PriorityQueue {
    constructor() {
        this.pq = [null];
        this.n = 0;
    }
    comparator(a, b) {
        return this.pq[a][2] > this.pq[b][2];
    }
    size() {
        return this.n;
    }
    swim(n) {
        while (n > 1 && this.comparator(n >> 1, n)) {
            this.exch(n >> 1, n);
            n = n >> 1;
        }
    }
    insert(value) {
        this.pq[++this.n] = value;
        this.swim(this.n);
    }
    sink(n) {
        while (n * 2 <= this.n) {
            let i = n * 2;
            if (i < this.n && this.comparator(i, i + 1)) i++;
            if (this.comparator(i, n)) break;
            this.exch(i, n);
            n = i;
        }
    }
    poll() {
        const result = this.pq[1];
        this.pq[1] = this.pq[this.n--];
        this.sink(1);
        return result;
    }
    exch(a, b) {
        const temp = this.pq[a];
        this.pq[a] = this.pq[b];
        this.pq[b] = temp;
    }
}

/**
 * @param {number[][]} heightMap
 * @return {number}
 */
var trapRainWater = function(heightMap) {
    const m = heightMap.length, n = heightMap[0].length, pq = new PriorityQueue();
    const visited = Array.from(new Array(m), () => new Array(n).fill(false)), dirs = [-1, 0, 1, 0, -1];
    let ans = 0;
    for(let i=1;i<m-1;i++){
        pq.insert([i, 0, heightMap[i][0]]);
        pq.insert([i, n-1, heightMap[i][n-1]]);
    }
    for(let j=1;j<n-1;j++){
        pq.insert([0, j, heightMap[0][j]]);
        pq.insert([m-1, j, heightMap[m-1][j]]);
    }
    while(pq.size()>0){
        const cur = pq.poll();
        for(let i=0;i<4;i++){
            const nx = cur[0] + dirs[i], ny = cur[1] + dirs[i+1];
            if(nx > 0 && nx < m - 1 && ny > 0 && ny < n - 1 && !visited[nx][ny]){
                visited[nx][ny] = true;
                ans += Math.max(0, cur[2] - heightMap[nx][ny]);
                pq.insert([nx, ny, Math.max(cur[2],heightMap[nx][ny])]);
            }
        }
    }
    return ans;
};
```