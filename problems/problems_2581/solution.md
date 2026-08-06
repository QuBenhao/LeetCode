# [Python/Go] 换根dp

> slug: pythongoc-huan-gen-dp-by-himymben-csne
> date: 2024-02-29
> tags: C, Go, Java, Python3, TypeScript
> question: Count Number of Possible Root Nodes (count-number-of-possible-root-nodes)
> url: https://leetcode.cn/problems/count-number-of-possible-root-nodes/solutions/yYhvQt/pythongoc-huan-gen-dp-by-himymben-csne/

---

> Problem: [2581. 统计可能的树根数目](https://leetcode.cn/problems/count-number-of-possible-root-nodes/description/)

[TOC]

# 思路

> 从[灵神那里](https://leetcode.cn/problems/count-number-of-possible-root-nodes/solutions/2147714/huan-gen-dppythonjavacgo-by-endlesscheng-ccwy/?envType=daily-question&envId=2024-02-29)学会的

# 解题方法

> 以一个值为根建树以后，猜对的数量根据不停换根而变化，统计满足答案的变化数

# 复杂度

时间复杂度:
> $O(n+m)$

空间复杂度:
> $O(n+m)$



# Code
```Python3 []
class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        gs = defaultdict(set)
        for a, b in guesses:
            gs[a].add(b)
        
        # 统计以root为根，猜对的数量
        def dfs1(node, parent):
            cnts = 0
            if node in gs[parent]:
                cnts += 1
            for child in graph[node]:
                if child != parent:
                    cnts += dfs1(child, node)
            return cnts

        # 统计交换其中的父子关系，猜对数量的变化
        def dfs2(node, parent, cur):
            res = cur >= k
            for child in graph[node]:
                if child != parent:
                    # 以child为父节点，node为子节点，child的其他子节点父子关系不变，node的父节点、其他子节点的父子关系不变
                    # 所以变化的只有node是child的父节点之前的猜测的正确性
                    res += dfs2(child, node, cur - (child in gs[node]) + (node in gs[child])) 
            return res
        
        return dfs2(0, -1, dfs1(0, -1))
```
```Go []
func rootCount(edges [][]int, guesses [][]int, k int) int {
    graph := make([][]int, len(edges) + 1)
    for _, e := range edges {
        a, b := e[0], e[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }

	type pair struct{ x, y int }
	gs := make(map[pair]int, len(guesses))
	for _, p := range guesses { // guesses 转成哈希表
		gs[pair{p[0], p[1]}] = 1
	}

    var dfs1 func(int, int) int
    dfs1 = func(node, parent int) (ans int) {
        for _, child := range graph[node] {
            if child != parent {
                if gs[pair{node, child}] == 1 {
                    ans++
                }
                ans += dfs1(child, node)
            }
        }
        return
    }

    var dfs2 func(int, int, int) int
    dfs2 = func(node, parent, cur int) (ans int) {
        if cur >= k {
            ans++
        }
        for _, child := range graph[node] {
            if child != parent {
                ans += dfs2(child, node, cur - gs[pair{node, child}] + gs[pair{child, node}])
            }
        }
        return
    }
    
    return dfs2(0, -1, dfs1(0, -1))
}
```