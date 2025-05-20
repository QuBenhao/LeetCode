package problem2065

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func maximalPathQuality(values []int, edges [][]int, maxTime int) (ans int) {
	n := len(values)
	type edge struct{ to, time int }
	g := make([][]edge, n)
	for _, e := range edges {
		x, y, t := e[0], e[1], e[2]
		g[x] = append(g[x], edge{y, t})
		g[y] = append(g[y], edge{x, t})
	}

	// Dijkstra 算法
	dis := make([]int, n)
	for i := 1; i < n; i++ {
		dis[i] = math.MaxInt
	}
	h := hp{{0, 0}}
	for len(h) > 0 {
		p := heap.Pop(&h).(pair)
		dx := p.dis
		x := p.x
		if dx > dis[x] { // x 之前出堆过
			continue
		}
		for _, e := range g[x] {
			y := e.to
			newDis := dx + e.time
			if newDis < dis[y] {
				dis[y] = newDis // 更新 x 的邻居的最短路
				heap.Push(&h, pair{newDis, y})
			}
		}
	}

	vis := make([]bool, n)
	vis[0] = true
	var dfs func(int, int, int)
	dfs = func(x, sumTime, sumValue int) {
		if x == 0 {
			ans = max(ans, sumValue)
			// 注意这里没有 return，还可以继续走
		}
		for _, e := range g[x] {
			y, t := e.to, e.time
			// 相比方法一，这里多了 dis[y]
			if sumTime+t+dis[y] > maxTime {
				continue
			}
			if vis[y] {
				dfs(y, sumTime+t, sumValue)
			} else {
				vis[y] = true
				// 每个节点的价值至多算入价值总和中一次
				dfs(y, sumTime+t, sumValue+values[y])
				vis[y] = false // 恢复现场
			}
		}
	}
	dfs(0, 0, values[0])
	return ans
}

type pair struct{ dis, x int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].dis < h[j].dis }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hp) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var values []int
	var edges [][]int
	var maxTime int

	if err := json.Unmarshal([]byte(inputValues[0]), &values); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &maxTime); err != nil {
		log.Fatal(err)
	}

	return maximalPathQuality(values, edges, maxTime)
}
