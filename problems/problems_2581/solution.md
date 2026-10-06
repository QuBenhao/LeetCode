# [Python/Go] Rerooting DP

> slug: pythongoc-huan-gen-dp-by-himymben-csne
> date: 2024-02-29
> tags: C, Go, Java, Python3, TypeScript
> question: Count Number of Possible Root Nodes (count-number-of-possible-root-nodes)
> url: https://leetcode.cn/problems/count-number-of-possible-root-nodes/solutions/yYhvQt/pythongoc-huan-gen-dp-by-himymben-csne/

---

> Problem: [2581. 统计可能的树根数目](https://leetcode.cn/problems/count-number-of-possible-root-nodes/description/)

[TOC]

# Intuition

> Learned from [灵神](https://leetcode.cn/problems/count-number-of-possible-root-nodes/solutions/2147714/huan-gen-dppythonjavacgo-by-endlesscheng-ccwy/?envType=daily-question&envId=2024-02-29).

# Approach

> Build the tree with one root, then track how the number of correct guesses changes as the root moves. Count the root choices that satisfy the requirement.

# Complexity

Time complexity:
> $O(n+m)$

Space complexity:
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
        
        # Count correct guesses when the tree is rooted at root
        def dfs1(node, parent):
            cnts = 0
            if node in gs[parent]:
                cnts += 1
            for child in graph[node]:
                if child != parent:
                    cnts += dfs1(child, node)
            return cnts

        # Track the change in correct guesses when reversing this parent-child relationship
        def dfs2(node, parent, cur):
            res = cur >= k
            for child in graph[node]:
                if child != parent:
                    # Make child the parent and node the child; relationships with child's other children and with node's parent and other children stay unchanged
                    # Thus only the correctness of the guess that node is child's parent changes
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
	for _, p := range guesses { // Convert guesses to a hash table
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
