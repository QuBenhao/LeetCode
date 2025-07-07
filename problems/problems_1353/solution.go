package problem1353

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maxEvents(events [][]int) (ans int) {
	slices.SortFunc(events, func(a, b []int) int { return a[1] - b[1] })
	mx := events[len(events)-1][1]
	fa := make([]int, mx+2)
	for i := range fa {
		fa[i] = i
	}

	var find func(int) int
	find = func(x int) int {
		if fa[x] != x {
			fa[x] = find(fa[x])
		}
		return fa[x]
	}

	for _, event := range events {
		x := find(event[0])
		if x <= event[1] {
			ans++
			fa[x] = x + 1
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var events [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &events); err != nil {
		log.Fatal(err)
	}

	return maxEvents(events)
}
