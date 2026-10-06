# [Python/Go] Offline queries + trie with deletion (based on 421)

> slug: pythongo-chi-xian-cha-xun-dai-shan-chu-d-h57x
> date: 2021-11-15
> tags: Go, Python, Python3
> question: Maximum Genetic Difference Query (maximum-genetic-difference-query)
> url: https://leetcode.cn/problems/maximum-genetic-difference-query/solutions/BwLgMk/pythongo-chi-xian-cha-xun-dai-shan-chu-d-h57x/

---
### Approach
Use the trie from problem 421 to answer the maximum-XOR queries at each node. Recursively process all children, then remove the current node from the trie.

### Code

```Python3 []
MAX_BIT = len(bin(200000)) - 2
class Solution:
    def maxGeneticDifference(self, parents: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        # Offline queries
        query_map = defaultdict(list)
        for i,query in enumerate(queries):
            query_map[query[0]].append((i, query[1]))
        r = -1
        # Build the tree
        mapping = defaultdict(list)
        for i, parent in enumerate(parents):
            if parent == -1:
                r = i
            else:
                mapping[parent].append(i)
        # Traverse the tree, inserting into, querying, and deleting from the trie
        trie = Trie()
        def dfs(node):
            trie.insert(node)
            for i, q in query_map[node]:
                ans[i] = trie.find(q)
            for children in mapping[node]:
                dfs(children)
            trie.delete(node)
        dfs(r)
        return ans

class Trie:
    def __init__(self):
        self.root = dict()
    
    def insert(self, num):
        node = self.root
        for i in range(MAX_BIT, -1, -1):
            b = (num >> i) & 1
            if b in node:
                node[b][1] += 1
            else:
                node[b] = [dict(), 1]
            node = node[b][0]
    
    def find(self, num):
        node = self.root
        ans = 0
        for i in range(MAX_BIT, -1, -1):
            b = (num >> i) & 1
            if b ^ 1 in node and node[b ^ 1][1]:
                node = node[b ^ 1][0]
                ans += 1 << i
            else:
                node = node[b][0]
        return ans
    
    def delete(self, num):
        node = self.root
        for i in range(MAX_BIT, -1, -1):
            b = (num >> i) & 1
            node[b][1] -= 1
            node = node[b][0]

```
```Go []
type Trie struct{
    zero *Trie
    zeroCnts int
    one *Trie
    oneCnts int
}

func (t *Trie) insert(num int){
    node := t
    for i := 17; i >= 0; i-- {
        if b := (num >> i) & 1; b == 0 {
            if node.zero == nil {
                node.zero = &Trie{}
            }
            node.zeroCnts++
            node = node.zero
        } else {
            if node.one == nil {
                node.one = &Trie{}
            }
            node.oneCnts++
            node = node.one
        }
    }
}

func (t *Trie) find(num int) (ans int){
    node := t
    for i := 17; i >= 0; i-- {
        if b := (num >> i) & 1; b == 0 {
            if node.oneCnts > 0 {
                node = node.one
                ans += 1 << i
            } else {
                node = node.zero
            }
        } else {
            if node.zeroCnts > 0 {
                node = node.zero
                ans += 1 << i
            }else{
                node = node.one
            }
        }
    }
    return ans
}

func (t *Trie) delete(num int){
    node := t
    for i := 17; i >= 0; i-- {
        if b := (num >> i) & 1; b == 0 {
            node.zeroCnts--
            node = node.zero
        } else {
            node.oneCnts--
            node = node.one
        }
    }
}


func maxGeneticDifference(parents []int, queries [][]int) []int {
    ans := make([]int, len(queries))
    // Offline queries
    type query struct{
        i int
        v int
    }
    queryMap := map[int][]query{}
    for i, v := range queries {
        queryMap[v[0]] = append(queryMap[v[0]], query{i, v[1]})
    }
    // Build the tree
    root := -1
    tree := map[int][]int{}
    for i, p := range parents {
        if p == -1 {
            root = i
        } else {
            tree[p] = append(tree[p], i)
        }
    }

    // Recurse over the tree and maintain the trie
    trie := Trie{}
    var dfs func(int)
    dfs = func(node int) {
        trie.insert(node)
        for _, qy := range queryMap[node] {
            ans[qy.i] = trie.find(qy.v)
        }
        for _, child := range tree[node] {
            dfs(child)
        }
        trie.delete(node)
    }
    dfs(root)
    return ans
}
```
