package problem2462

import (
	"container/heap"
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

func totalCost(costs []int, k, candidates int) (ans int64) {
	n := len(costs)
	if candidates*2+k > n {
		slices.Sort(costs)
		for _, x := range costs[:k] {
			ans += int64(x)
		}
		return
	}

	pre := hp{costs[:candidates]}
	suf := hp{costs[len(costs)-candidates:]}
	heap.Init(&pre)
	heap.Init(&suf)
	for i, j := candidates, n-1-candidates; k > 0; k-- {
		if pre.IntSlice[0] <= suf.IntSlice[0] {
			ans += int64(pre.replace(costs[i]))
			i++
		} else {
			ans += int64(suf.replace(costs[j]))
			j--
		}
	}
	return
}

type hp struct{ sort.IntSlice }

func (h *hp) Push(v any)        { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() any          { a := h.IntSlice; v := a[len(a)-1]; h.IntSlice = a[:len(a)-1]; return v }
func (h *hp) replace(v int) int { top := h.IntSlice[0]; h.IntSlice[0] = v; heap.Fix(h, 0); return top }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var costs []int
	var k int
	var candidates int

	if err := json.Unmarshal([]byte(inputValues[0]), &costs); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &candidates); err != nil {
		log.Fatal(err)
	}

	return totalCost(costs, k, candidates)
}
