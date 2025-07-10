package problem3169

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func countDays(days int, meetings [][]int) (ans int) {
	sort.Slice(meetings, func(i, j int) bool {
		return meetings[i][0] < meetings[j][0]
	})
	cur := 0
	for _, meeting := range meetings {
		start, end := meeting[0], meeting[1]
		if start > cur {
			ans += start - cur - 1
		}
		cur = max(cur, end)
	}
	ans += days - cur
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var days int
	var meetings [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &days); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &meetings); err != nil {
		log.Fatal(err)
	}

	return countDays(days, meetings)
}
