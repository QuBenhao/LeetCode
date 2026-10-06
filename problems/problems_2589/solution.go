package problem2589

import (
	"encoding/json"
	"log"
	"slices"
	"sort"
	"strings"
)

func findMinimumTime(tasks [][]int) int {
	slices.SortFunc(tasks, func(a, b []int) int { return a[1] - b[1] })
	// The stack stores inclusive interval endpoints and the cumulative interval length from the bottom through each entry
	type tuple struct{ l, r, s int }
	st := []tuple{{-2, -2, 0}} // Sentinel that does not overlap any interval
	for _, p := range tasks {
		start, end, d := p[0], p[1], p[2]
		i := sort.Search(len(st), func(i int) bool { return st[i].l >= start }) - 1
		d -= st[len(st)-1].s - st[i].s // Subtract time points when the computer is already running
		if start <= st[i].r {          // start lies inside st[i]
			d -= st[i].r - start + 1 // Subtract time points when the computer is already running
		}
		if d <= 0 {
			continue
		}
		for end-st[len(st)-1].r <= d { // Fill the interval's suffix with the remaining d time points
			top := st[len(st)-1]
			st = st[:len(st)-1]
			d += top.r - top.l + 1 // Merge intervals
		}
		st = append(st, tuple{end - d + 1, end, st[len(st)-1].s + d})
	}
	return st[len(st)-1].s
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var tasks [][]int

	if err := json.Unmarshal([]byte(values[0]), &tasks); err != nil {
		log.Fatal(err)
	}

	return findMinimumTime(tasks)
}
