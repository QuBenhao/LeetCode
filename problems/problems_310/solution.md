# [Python/Java/JavaScript/Go] Topological sort + BFS

> slug: pythonjavajavascriptgo-by-himymben-akh6
> date: 2022-04-05
> tags: Go, Java, JavaScript, Python, Python3
> question: Minimum Height Trees (minimum-height-trees)
> url: https://leetcode.cn/problems/minimum-height-trees/solutions/I1r5I6/pythonjavajavascriptgo-by-himymben-akh6/

---
### Approach
1. The meaning of degree 1
A node of degree 1 generally cannot be an answer, except when there are only two nodes.
Its sole neighbor is always one step closer to every other node. Rooting the tree at that neighbor therefore gives a smaller (or equal) minimum height than rooting it at the degree-1 node.
After removing all degree-1 nodes, the graph has updated degrees and new degree-1 nodes. Repeat the same reasoning.

2. Why there can be at most two answer nodes
Proof by contradiction:
Suppose three roots a, b, and c produce minimum-height trees of height h.
There is a node d at distance h from a. Both b and c must lie on the path from d to a; otherwise, their distance from d would exceed h. Their distances from d are therefore less than h.
Likewise, there must be a node e at distance h from b, with a and c lying on the path from e to b.
This gives the following configuration:
a --- b --- d
b --- a --- e
Clearly, the only possible arrangement is:
e --- a --- b --- d, so that a lies on the path be and b lies on the path ad.
Now c must lie on both the path ad and the path be. Therefore:
e --- a - c - b ---- d
The distance from c to d is less than h, and so is the distance from c to e.
We still need a node at distance h from c whose distances to both a and b are at most h.
No location for that node can satisfy these distance requirements.

### Code

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
