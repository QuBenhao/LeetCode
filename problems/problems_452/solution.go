package problem452

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func findMinArrowShots(points [][]int) int {
	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})
	cur, ans := points[0][1], 1
	for _, point := range points {
		if point[0] > cur {
			ans++
			cur = point[1]
		}
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(values[0]), &points); err != nil {
		log.Fatal(err)
	}

	return findMinArrowShots(points)
}
