package problem3111

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func minRectanglesToCoverPoints(points [][]int, w int) (ans int) {
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})
	for idx := 0; idx < len(points); {
		ans++
		cur := points[idx][0] + w
		for idx < len(points) && points[idx][0] <= cur {
			idx++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int
	var w int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &w); err != nil {
		log.Fatal(err)
	}

	return minRectanglesToCoverPoints(points, w)
}
