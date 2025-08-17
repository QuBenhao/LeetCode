package problem3650

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func minCost(n int, edges [][]int) int {
	graph := make([]map[int]int, n)
	for _, edge := range edges {
		u, v, cost := edge[0], edge[1], edge[2]
		if graph[u] == nil {
			graph[u] = make(map[int]int)
		}
		if graph[v] == nil {
			graph[v] = make(map[int]int)
		}
		if _, exists := graph[u][v]; !exists || graph[u][v] > cost {
			graph[u][v] = cost
		}
		if _, exists := graph[v][u]; !exists || graph[v][u] > cost*2 {
			graph[v][u] = cost * 2
		}
	}
	dist := make([]int, n)
	for i := range dist {
		dist[i] = math.MaxInt32
	}
	dist[0] = 0
	pq := hp{{0, 0}} // pair{distance, index}
	heap.Init(&pq)
	for len(pq) > 0 {
		p := heap.Pop(&pq).(pair)
		d, i := p.d, p.i
		if i == n-1 {
			return d
		}
		if d > dist[i] {
			continue
		}
		for j, cost := range graph[i] {
			if nd := d + cost; nd < dist[j] {
				dist[j] = nd
				heap.Push(&pq, pair{nd, j})
			}
		}
	}
	return -1 // 如果没有到达终点，返回-1
}

type pair struct{ d, i int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].d < h[j].d }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(x any) {
	*h = append(*h, x.(pair))
}
func (h *hp) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}

	return minCost(n, edges)
}
