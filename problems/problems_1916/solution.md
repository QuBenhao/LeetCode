# [Python/Java/Go] 树状动态规划求拓扑方案数 + 乘法逆元求组合数

> Author: Benhao
> Date: 2021-06-27
> Upvotes: 6
> Tags: Go, Java, Python, Python3

---

### 解题思路
学习了……[来源](https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/discuss/1299545/Python3-post-order-dfs)

### 代码

```python3
class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        connect = defaultdict(list)
        for i,num in enumerate(prevRoom):
            connect[num].append(i)

        # 返回:元素个数,拓扑排序方案数
        def dfs(idx):
            nodes, ans = 0, 1
            for subnode in connect[idx]:
                nodes_, ans_ = dfs(subnode)
                nodes += nodes_
                # 因为当前的拓扑排序方案数不影响加入该子树后的拓扑排序方案数，所以是乘法叠加
                # 新的拓扑排序方案数为: 当前的拓扑排序方案数 * 从nodes个位置里选nodes_个位置分配给该子树 * 子树的拓扑排序方案数
                ans = (ans * comb(nodes, nodes_) * ans_) % (10 ** 9 + 7)
            # 加上根节点
            return nodes + 1, ans
        
        return dfs(0)[1]
```
```Java []
class Solution {
    private static final int mod = (int)1e9 + 7;
    private static final int[] fac = new int[100005];
    private static final int[] inv = new int[100005];
    static{
        long f = 1;
        for(int i=1;i<=100000;i++){
            f = f * i % mod;
            fac[i] = (int)f;
            inv[i] = quickPower(fac[i], mod - 2);
        }
    }

    private Map<Integer, List<Integer>> graph;

    public int waysToBuildRooms(int[] prevRoom) {
        graph = new HashMap<>();
        for(int i=0;i<prevRoom.length;i++){
            List<Integer> list = graph.getOrDefault(prevRoom[i], new ArrayList<>());
            list.add(i);
            graph.put(prevRoom[i], list);
        }
        return dfs(0)[1];
    }

    private int[] dfs(int i){
        int size = 0;
        long res = 1;
        if(graph.containsKey(i)){
            for(Integer child: graph.get(i)){
                int[] cur = dfs(child);
                size += cur[0];
                if (size > cur[0]){
                    res = res * fac[size] % mod;
                    res = res * inv[size-cur[0]] % mod;
                    res = res * inv[cur[0]] % mod;
                }
                res = res * cur[1] % mod;
            }
        }
        return new int[]{++size, (int)res};
    }

    private static int quickPower(int x, int n) {
        long ans = 1, lx = (long)x;
        while(n > 0){
            if((n & 1) == 1)
                ans = ans * lx % mod;
            lx = lx * lx % mod;
            n >>= 1;
        }
        return (int)ans;
    }
}
```
```Go []
const mod int64 = 1000000007
func waysToBuildRooms(prevRoom []int) int {
    n := len(prevRoom)
    fac, inv, graph := make([]int64, n + 1), make([]int64, n + 1), map[int][]int{}
    var f int64 = 1
    for i := 1; i <= n; i++ {
        f = f * int64(i) % mod
        fac[i] = f
        inv[i] = quickPower(f, mod - 2)
        graph[prevRoom[i-1]] = append(graph[prevRoom[i-1]], i-1)
    }

    var dfs func(i int) []int64
    dfs = func(i int) []int64 {
        var size, res int64
        size, res = 0, 1
        for _, child := range graph[i] {
            cur := dfs(child)
            size += cur[0]
            if size > cur[0] {
                res = (((res * cur[1] % mod) * fac[size] % mod) * inv[cur[0]] % mod) * inv[size - cur[0]] % mod
            } else {
                res = res * cur[1] % mod
            }
        }
        return []int64{size + 1, res}
    }

    return int(dfs(0)[1])
}

func quickPower(x, y int64) int64 {
    var res int64 = 1
    for ; y > 0; y>>=1 {
        if (y & 1) == 1 {
            res = res * x % mod
        }
        x = x * x % mod
    }
    return res
}
```