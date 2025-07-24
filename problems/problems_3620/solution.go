package problem3620

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"strings"
)

func findMaxPathScore(edges [][]int, online []bool, k int64) int {
	n := len(online)
	graph := make([][][]int, n)
	right := 0
	for _, edge := range edges {
		u, v, c := edge[0], edge[1], edge[2]
		if online[u] && online[v] {
			graph[u] = append(graph[u], []int{v, c})
			right = max(right, c)
		}
	}

	helper := func(minCost int) bool {
		distance := make([]int64, n)
		for i := range distance {
			distance[i] = math.MaxInt64
		}
		distance[0] = 0
		pq := &hp{{0, 0}} // distance, node
		for pq.Len() > 0 {
			cur := heap.Pop(pq).(Pair)
			if cur.node == n-1 {
				return true
			}
			if cur.distance > distance[cur.node] {
				continue
			}
			for _, next := range graph[cur.node] {
				nextNode, nextCost := next[0], next[1]
				if nextCost < minCost {
					continue
				}
				newDistance := cur.distance + int64(nextCost)
				if newDistance <= k && newDistance < distance[nextNode] {
					distance[nextNode] = newDistance
					heap.Push(pq, Pair{newDistance, nextNode})
				}
			}
		}
		return false
	}

	left := -1
	for left < right {
		mid := (left + right + 1) / 2
		if helper(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	return left
}

type Pair struct {
	distance int64
	node     int
}
type hp []Pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].distance < h[j].distance }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(x any) {
	*h = append(*h, x.(Pair))
}
func (h *hp) Pop() any {
	old := *h
	n := len(old)
	item := old[n-1]
	*h = old[0 : n-1]
	return item
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var edges [][]int
	var online []bool
	var k int64

	if err := json.Unmarshal([]byte(inputValues[0]), &edges); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &online); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return findMaxPathScore(edges, online, k)
}
