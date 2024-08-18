package problemLCR_074

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func merge(intervals [][]int) (ans [][]int) {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})
	ans = append(ans, intervals[0])
	for _, interval := range intervals {
		a, b := interval[0], interval[1]
		if a <= ans[len(ans)-1][1] {
			ans[len(ans)-1][1] = max(ans[len(ans)-1][1], b)
		} else {
			ans = append(ans, interval)
		}
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var intervals [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &intervals); err != nil {
		log.Fatal(err)
	}

	return merge(intervals)
}
