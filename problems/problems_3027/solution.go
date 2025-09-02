package problem3027

import (
	"encoding/json"
	"log"
	"math"
	"slices"
	"strings"
)

func numberOfPairs(points [][]int) (ans int) {
	slices.SortFunc(points, func(a, b []int) int {
		if a[0] == b[0] {
			return b[1] - a[1]
		}
		return a[0] - b[0]
	})
	n := len(points)
	for i, point := range points {
		y := point[1]
		maxY := math.MinInt32
		for j := i + 1; j < n; j++ {
			if y >= points[j][1] && points[j][1] > maxY {
				maxY = points[j][1]
				ans++
				if maxY == y {
					break
				}
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
