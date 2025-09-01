package problem3025

import (
	"encoding/json"
	"log"
	"sort"
	"strings"
)

func numberOfPairs(points [][]int) (ans int) {
	sort.Slice(points, func(i, j int) bool {
		if points[i][0] != points[j][0] {
			return points[i][0] < points[j][0]
		}
		return points[i][1] > points[j][1]
	})
	n := len(points)
	for i, p1 := range points {
		maxY := -1
		for j := i + 1; j < n; j++ {
			if p1[1] >= points[j][1] && points[j][1] > maxY {
				maxY = points[j][1]
				ans++
			}
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}

	return numberOfPairs(points)
}
