package problem2070

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func maximumBeauty(items [][]int, queries []int) []int {
	slices.SortFunc(items, func(a, b []int) int { return a[0] - b[0] })
	n := len(queries)
	ans := make([]int, n)
	idxes := make([]int, n)
	for i := range idxes {
		idxes[i] = i
	}
	slices.SortFunc(idxes, func(a, b int) int { return queries[a] - queries[b] })
	i, curMax := 0, 0
	for _, idx := range idxes {
		q := queries[idx]
		for i < len(items) && items[i][0] <= q {
			curMax = max(curMax, items[i][1])
			i++
		}
		ans[idx] = curMax
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var items [][]int
	var queries []int

	if err := json.Unmarshal([]byte(inputValues[0]), &items); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return maximumBeauty(items, queries)
}
