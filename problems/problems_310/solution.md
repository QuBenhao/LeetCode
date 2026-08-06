# [Python/Java/JavaScript/Go] 拓扑 + BFS

> slug: pythonjavajavascriptgo-by-himymben-akh6
> date: 2022-04-05
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Height Trees (minimum-height-trees)
> url: https://leetcode.cn/problems/minimum-height-trees/solutions/I1r5I6/pythonjavajavascriptgo-by-himymben-akh6/

---
### 解题思路
1. 入度为1的意义
入度为1的点基本不会作为最终答案【除了只有两个点的情况】，
因为与它相连的点（入度为1所以只有这一个点）到其他点的距离，永远比它到这些点的距离小1，以相连点为根会比入度为1的点为根最小高度更小（小于等于）。
我们刨去所有入度为1的点以后，整个图有了一个新的入度，又同样有了新的一些入度为1的点，重复上面的讨论。

2. 为什么答案的点最多有两个
反证法：
假设有三个点a、b、c作为根有最小生成树，最小高度树为h。
存在点d到a的距离为h，那么b、c只能在d到a的路径上，否则d到b或c的距离会大于h，那么d到b、c的点是不足h的，
所以必须同样存在点e到b的距离为h，a、c只能在e到b的路径上。
于是我们有了这样一个概念:
a --- b --- d
b --- a --- e
很明显只有这样构造:
e --- a --- b --- d才能满足a在be的路径上，b在ad的路径上。
那么此时c要在ad的路径上，又要在be的路径上，于是:
e --- a - c - b ---- d
我们发现什么，c到d的距离不足h，到e的距离也不足h。
还需要一个到c距离为h的点，这个点还要满足a、b到它的距离不大于h。
无论这个点在哪里，都不能保证这个距离。

### 代码

```Python3 []
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree, connect = [0] * n, defaultdict(list)
        for a, b in edges:
            in_degree[a] += 1
            in_degree[b] += 1
            connect[a].append(b)
            connect[b].append(a)
        nodes = [i for i, v in enumerate(in_degree) if v <= 1]
        while n > 2:
            n -= len(nodes)
            nxt = []
            for node in nodes:
                for other in connect[node]:
                    in_degree[other] -= 1
                    if in_degree[other] == 1:
                        nxt.append(other)
            nodes = nxt
        return nodes
```
```Java []
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        int[] in = new int[n];
        Map<Integer, List<Integer>> connect = new HashMap<>();
        for(int[] edge: edges) {
            in[edge[0]]++;
            in[edge[1]]++;
            List<Integer> l0 = connect.getOrDefault(edge[0], new ArrayList<>());
            l0.add(edge[1]);
            connect.put(edge[0], l0);
            List<Integer> l1 = connect.getOrDefault(edge[1], new ArrayList<>());
            l1.add(edge[0]);
            connect.put(edge[1], l1);
        }
        List<Integer> nodes = new ArrayList<>();
        for(int i = 0; i < n; i++)
            if(in[i] < 2)
                nodes.add(i);
        while(n > 2) {
            n -= nodes.size();
            List<Integer> nxt = new ArrayList<>();
            for(int node: nodes) {
                for(int other: connect.get(node)) {
                    in[other]--;
                    if(in[other] == 1)
                        nxt.add(other);
                }
            }
            nodes = nxt;
        }
        return nodes;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
    const degree = new Array(n).fill(0), connect = new Map()
    for(const edge of edges) {
        const a = edge[0], b = edge[1]
        degree[a]++
        degree[b]++
        var l0, l1
        if(connect.has(a))
            l0 = connect.get(a)
        else
            l0 = new Array()
        l0.push(b)
        connect.set(a, l0)
        if(connect.has(b))
            l1 = connect.get(b)
        else
            l1 = new Array()
        l1.push(a)
        connect.set(b, l1)
    }
    let nodes = new Array()
    for(let i = 0; i < n; i++)
        if(degree[i] < 2)
            nodes.push(i)
    while(n > 2) {
        n -= nodes.length
        const nxt = new Array()
        for(const node of nodes) {
            for(const other of connect.get(node)) {
                degree[other]--
                if(degree[other] == 1)
                    nxt.push(other)
            }
        }
        nodes = nxt
    }
    return nodes
};
```
```Go []
func findMinHeightTrees(n int, edges [][]int) (nodes []int) {
    in, connect := make([]int, n), map[int][]int{}
    for _, edge := range edges {
        a, b := edge[0], edge[1]
        in[a]++
        in[b]++
        connect[a] = append(connect[a], b)
        connect[b] = append(connect[b], a)
    }
    for i := 0; i < n; i++ {
        if in[i] < 2 {
            nodes = append(nodes, i)
        }
    }
    for n > 2 {
        s := len(nodes)
        n -= s
        for _, node := range nodes {
            for _, other := range connect[node] {
                in[other]--
                if in[other] == 1 {
                    nodes = append(nodes, other)
                }
            }
        }
        nodes = nodes[s:]
    }
    return nodes
}
```