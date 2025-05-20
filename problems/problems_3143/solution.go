package problem3143

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func maxPointsInsideSquare(points [][]int, s string) (ans int) {
	idxMap := make([]int, 26)
	for i := 0; i < 26; i++ {
		idxMap[i] = math.MaxInt
	}
	minD := math.MaxInt
	for i, point := range points {
		c := s[i] - 'a'
		if cur := max(abs(point[0]), abs(point[1])); cur < idxMap[c] {
			minD = min(minD, idxMap[c])
			idxMap[c] = cur
		} else {
			minD = min(minD, cur)
		}
	}
	for _, m := range idxMap {
		if m < minD {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var points [][]int
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &points); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &s); err != nil {
		log.Fatal(err)
	}

	return maxPointsInsideSquare(points, s)
}
