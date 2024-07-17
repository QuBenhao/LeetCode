package problem3112

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func minimumTime(n int, edges [][]int, disappear []int) []int {
	graph := make([][]pair, n)
	for _, edge := range edges {
		u, v, w := edge[0], edge[1], edge[2]
		graph[u] = append(graph[u], pair{w, v})
		graph[v] = append(graph[v], pair{w, u})
	}
	dis := make([]int, n)
	for i := range dis {
		dis[i] = -1
	}
	dis[0] = 0
	pq := hp{{0, 0}}
	for len(pq) > 0 {
		cur := heap.Pop(&pq).(pair)
		w, u := cur.dis, cur.x
		if dis[u] < w {
			continue
		}
		for _, e := range graph[u] {
			v, dw := e.x, e.dis
			if nw := w + dw; nw < disappear[v] && (dis[v] == -1 || nw < dis[v]) {
				dis[v] = nw
				heap.Push(&pq, pair{nw, v})
			}
		}
	}
	return dis
}

type pair struct{ dis, x int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].dis < h[j].dis }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hp) Pop() (v any)      { a := *h; *h, v = a[:len(a)-1], a[len(a)-1]; return }

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int
	var edges [][]int
	var disappear []int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &disappear); err != nil {
		log.Fatal(err)
	}

	return minimumTime(n, edges, disappear)
}
