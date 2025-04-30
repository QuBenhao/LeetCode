package problem743

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func networkDelayTime(times [][]int, n int, k int) int {
	type edge struct{ to, dis int }
	graph := map[int][]edge{}
	for _, t := range times {
		i, j, cost := t[0]-1, t[1]-1, t[2]
		graph[i] = append(graph[i], edge{j, cost})
	}
	visited := make([]int, n)
	for i := 0; i < n; i++ {
		visited[i] = math.MaxInt
	}
	pq := &hp{{0, k - 1}}
	for pq.Len() > 0 {
		node := heap.Pop(pq).(pair)
		if visited[node.x] < node.dis {
			continue
		}
		visited[node.x] = node.dis
		for _, neigh := range graph[node.x] {
			if visited[neigh.to] <= neigh.dis+node.dis {
				continue
			}
			visited[neigh.to] = neigh.dis + node.dis
			heap.Push(pq, pair{neigh.dis + node.dis, neigh.to})
		}
	}
	ans := -1
	for _, v := range visited {
		if v == math.MaxInt {
			return -1
		}
		ans = max(ans, v)
	}
	return ans
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
	var times [][]int
	var n int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &times); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &n); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return networkDelayTime(times, n, k)
}
