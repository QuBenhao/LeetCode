package problem857

import (
	"container/heap"
	"encoding/json"
	"log"
	"math"
	"sort"
	"strings"
)

func mincostToHireWorkers(quality, wage []int, k int) float64 {
	type pair struct{ q, w int }
	qw := make([]pair, len(quality))
	for i, q := range quality {
		qw[i] = pair{q, wage[i]}
	}
	sort.Slice(qw, func(i, j int) bool { a, b := qw[i], qw[j]; return a.w*b.q < b.w*a.q }) // Sort by r
	h := hp{make([]int, k)}
	sumQ := 0
	for i, p := range qw[:k] {
		h.IntSlice[i] = p.q
		sumQ += p.q
	}
	heap.Init(&h)
	ans := float64(sumQ*qw[k-1].w) / float64(qw[k-1].q) // Choose the k workers with the smallest r values as the current optimum
	for _, p := range qw[k:] {
		if p.q < h.IntSlice[0] { // sumQ can decrease, potentially improving the answer
			sumQ -= h.IntSlice[0] - p.q
			h.IntSlice[0] = p.q
			heap.Fix(&h, 0) // Update the heap top
			ans = math.Min(ans, float64(sumQ*p.w)/float64(p.q))
		}
	}
	return ans
}

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool { return h.IntSlice[i] > h.IntSlice[j] } // Max-heap
func (hp) Push(any)             {}                                       // This is unused, so its body can be empty
func (hp) Pop() (_ any)         { return }

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var quality []int
	var wage []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &quality); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &wage); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return mincostToHireWorkers(quality, wage, k)
}
