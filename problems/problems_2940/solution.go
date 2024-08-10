package problem2940

import (
	"container/heap"
	"encoding/json"
	"log"
	"strings"
)

func leftmostBuildingQueries(heights []int, queries [][]int) []int {
	ans := make([]int, len(queries))
	for i := range ans {
		ans[i] = -1
	}
	qs := make([][]pair, len(heights))
	for i, q := range queries {
		a, b := q[0], q[1]
		if a > b {
			a, b = b, a // 保证 a <= b
		}
		if a == b || heights[a] < heights[b] {
			ans[i] = b // a 直接跳到 b
		} else {
			qs[b] = append(qs[b], pair{heights[a], i}) // 离线询问
		}
	}

	h := hp{}
	for i, x := range heights {
		for h.Len() > 0 && h[0].h < x {
			// 堆顶的 heights[a] 可以跳到 heights[i]
			ans[heap.Pop(&h).(pair).i] = i
		}
		for _, p := range qs[i] {
			heap.Push(&h, p) // 后面再回答
		}
	}
	return ans
}

type pair struct{ h, i int }
type hp []pair

func (h hp) Len() int           { return len(h) }
func (h hp) Less(i, j int) bool { return h[i].h < h[j].h }
func (h hp) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *hp) Push(v any)        { *h = append(*h, v.(pair)) }
func (h *hp) Pop() any          { a := *h; v := a[len(a)-1]; *h = a[:len(a)-1]; return v }

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int
	var queries [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return leftmostBuildingQueries(heights, queries)
}
